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

@router.delete("/{id}")
def delete():
    return 
