from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError
from ..models import payments as model
from ..models import promotions as promo_model
from ..models.order_details import OrderDetail
from datetime import date
from decimal import Decimal


def create(db: Session, request):
    order_detail = db.query(OrderDetail).filter(OrderDetail.id == request.order_detail_id).first()
    if not order_detail:
        raise HTTPException(status_code=404, detail="Order detail not found")

    new_payment = model.Payment(
        card_info=request.card_info,
        transaction_status=request.transaction_status,
        payment_type=request.payment_type,
        payment_amount=order_detail.price*order_detail.quantity,
        order_id=request.order_id,
        order_detail_id=request.order_detail_id
    )

    try:
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_payment


def read_all(db: Session):
    try:
        result = db.query(model.Payment).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, payment_id: int):
    try:
        payment = db.query(model.Payment).filter(model.Payment.id == payment_id).first()
        if not payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment ID not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return payment


def update(db: Session, payment_id: int, request):
    try:
        payment = db.query(model.Payment).filter(model.Payment.id == payment_id)
        if not payment.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment ID not found!")
        update_data = request.dict(exclude_unset=True)
        payment.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return payment.first()


def delete(db: Session, payment_id: int):
    try:
        payment = db.query(model.Payment).filter(model.Payment.id == payment_id)
        if not payment.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment ID not found!")
        payment.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def apply_promo(db: Session, payment_id: int, promotion_id: int):
    try:
        payment = db.query(model.Payment).filter(model.Payment.id == payment_id).first()
        if not payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment ID not found!")
        promotion = db.query(promo_model.Promotion).filter(promo_model.Promotion.id == promotion_id).first()
        if not promotion:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found!")
        if promotion.exp_date < date.today():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Promotion has expired.")

        new_amount = payment.payment_amount * (Decimal("1.0") - promotion.discount)
        payment.payment_amount = new_amount.quantize(Decimal("0.01"))

        db.commit()
        db.refresh(payment)
        return payment
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
