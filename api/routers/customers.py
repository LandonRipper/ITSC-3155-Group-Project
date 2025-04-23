from http.client import HTTPException

from fastapi import APIRouter, Depends
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
def read_all():
    return


@router.get("/{id}", response_model=schema.Customer)
def read_one():
    return


@router.put("/{id}", response_model=schema.Customer)
def update():
    return

@router.delete("/{customer_id}", tags=["Customers"])
def delete(customer_id: int, db: Session = Depends(get_db)):
    customer = customer_controller.read_one(db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="User not found")
    return customer_controller.delete(db=db, customer_id=customer_id)

