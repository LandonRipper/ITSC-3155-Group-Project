

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import customers as controller
from ..schemas import customer as schema
from ..dependencies.database import engine, get_db
from ..controllers import customers as customer_controller
router = APIRouter(
    tags=['Customers'],
    prefix="/customers"
)
@router.post("/", response_model=schema.Customer, tags=["Customers"])
def create(customer: schema.CustomerCreate, db: Session = Depends(get_db)):
    return customer_controller.create(db=db, request = customer)

@router.get("/", response_model=list[schema.Customer])
def read_all(db: Session = Depends(get_db)):
    return customer_controller.read_all(db=db)


@router.get("/{customer_id}", response_model=schema.Customer)
def read_one(customer_id: int, db: Session = Depends(get_db)):
    customer = customer_controller.read_one(db=db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.put("/{customer_id}", response_model=schema.Customer)
def update(customer_id: int, customer: schema.Customer,db: Session = Depends(get_db)):
    return customer_controller.update(db=db, customer_id=customer_id, request=customer)

@router.delete("/{customer_id}", tags=["Customers"])
def delete(customer_id: int, db: Session = Depends(get_db)):
    customer = customer_controller.read_one(db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="User not found")
    return customer_controller.delete(db=db, customer_id=customer_id)

