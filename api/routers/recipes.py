from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import recipes as schema
from ..dependencies.database import engine, get_db
from ..controllers import customers as customer_controller

router = APIRouter(
    tags=["Recipes"],
    prefix="/recipes"
)


@router.post("/", response_model=schema.Recipe)
def create(request: schema.RecipeCreate, db: Session = Depends(get_db)):
    return customer_controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Recipe])
def read_all(db: Session = Depends(get_db)):
    return customer_controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Recipe)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return customer_controller.read_one(db, item_id)


@router.put("/{item_id}", response_model=schema.Recipe)
def update(item_id: int, request: schema.RecipeUpdate, db: Session = Depends(get_db)):
    return customer_controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return customer_controller.delete(db=db, item_id=item_id)
