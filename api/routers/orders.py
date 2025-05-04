from fastapi import APIRouter, Depends, FastAPI, status, Response, Query
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db
from datetime import date

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)


@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/orders/status/{tracking_number}", tags=["Orders"])
def read_status(tracking_number: int, db: Session = Depends(get_db)):
    return controller.get_order_status(db, tracking_number)

@router.put("/orders/status/{tracking_number}", tags=["Orders"])
def change_status(tracking_number: int, update: schema.OrderStatusUpdate, db: Session = Depends(get_db)):
    return controller.update_order_status(db, tracking_number, update)

@router.get("/", response_model=list[schema.Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/by-date-range/", response_model=list[schema.Order])
def read_by_date_range(
    from_date: date = Query(...),
    to_date: date = Query(...),
    db: Session = Depends(get_db)
):
    return controller.read_by_date_range(db=db, from_date=from_date, to_date=to_date)

@router.get("/revenue/by-date")
def revenue_by_date(target_date: date = Query(...), db: Session = Depends(get_db)):
    return controller.get_revenue_by_date(db=db, target_date=target_date)

@router.get("/{item_id}", response_model=schema.Order)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Order)
def update(item_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)

@router.post("/{customer_email}", response_model=schema.Order)
def create_with_account(request: schema.AccountOrderCreate, db: Session = Depends(get_db)):
    return controller.create_with_account(db=db, request=request, customer_email=request.customer_email)

