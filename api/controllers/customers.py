from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import customer as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_customer = model.Customer(
        name=request.name,
        email=request.email,
        phone_number=request.phone_number,
        address=request.address
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


def read_all(db: Session):
    try:
        result = db.query(model.Customer).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, customer_id: int):
    try:
        customer = db.query(model.Customer).filter(model.Customer.id == customer_id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer ID not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return customer


def update(db: Session, customer_id: int, request):
    try:
        customer = db.query(model.Customer).filter(model.Customer.id == customer_id)
        if not customer.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer ID not found!")
        update_data = request.dict(exclude_unset=True)
        customer.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return customer.first()


def delete(db: Session, customer_id: int):
    db_order  = db.query(model.Customer).filter(model.Customer.id == customer_id)
    db_order.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)