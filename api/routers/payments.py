from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import payments as controller
from ..schemas import payments as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Payments'],
    prefix="/payments"
)
@router.post("/", response_model=schema.Payment)
def create():
    return


@router.get("/", response_model=list[schema.Payment])
def read_all():
    return


@router.get("/{id}", response_model=schema.Payment)
def read_one():
    return


@router.put("/{id}", response_model=schema.Payment)
def update():
    return

@router.delete("/{id}")
def delete():
    return