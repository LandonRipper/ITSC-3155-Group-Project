from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import customers as controller
from ..schemas import customer as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Customers'],
    prefix="/customers"
)
@router.post("/", response_model=schema.Customer)
def create():
    return


@router.get("/", response_model=list[schema.Customer])
def read_all():
    return


@router.get("/{customer_id}", response_model=schema.Customer)
def read_one():
    return


@router.put("/{customer_id}", response_model=schema.Customer)
def update():
    return

@router.delete("/{customer_id}")
def delete():
    return 