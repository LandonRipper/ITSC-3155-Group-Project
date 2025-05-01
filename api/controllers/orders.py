from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as model
from ..models import customer as customer_model
from sqlalchemy.exc import SQLAlchemyError
from datetime import date
from ..models import payments as payment_model



def create(db: Session, request):
    customer = db.query(customer_model.Customer).filter(customer_model.Customer.name == request.customer_name).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found!")

    new_item = model.Order(
        customer_id=customer.id,
        description=request.description,
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item

def read_all(db: Session):
    try:
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def read_by_date_range(db: Session, from_date: date, to_date: date):
    try:
        orders = db.query(model.Order).filter(
            model.Order.order_date.between(from_date, to_date)
        ).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return orders

def get_total_revenue_by_date(db: Session, target_date: date):
    try:
        total = (
            db.query(func.sum(payment_model.Payment.payment_amount))
            .join(model.Order, payment_model.Payment.order_id == model.Order.id)
            .filter(func.date(model.Order.order_date) == target_date)
            .scalar()
        )

        return {"date": target_date, "total_revenue": total or 0}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

