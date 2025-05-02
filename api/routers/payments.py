
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import payments as controller
from ..schemas import payments as schema
from ..dependencies.database import engine, get_db
from ..schemas.payments import PaymentCreate

router = APIRouter(
    tags=['Payments'],
    prefix="/payments"
)
@router.post("/payments/", response_model=schema.PaymentCreate, status_code=201)
def create(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)



@router.get("/", response_model=list[schema.Payment])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{payment_id}", response_model=schema.Payment)
def read_one(payment_id: int, db: Session = Depends(get_db)):
    payment = controller.read_one(db, payment_id=payment_id)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found!")
    return payment


@router.put("/{payment_id}", response_model=schema.Payment)
def update(payment_id: int, request: schema.PaymentUpdate, db: Session = Depends(get_db)):
    updated = controller.update(db=db, payment_id=payment_id, request=request)
    if updated is None:
        raise HTTPException(status_code=404, detail="Payment not found!")
    return updated

@router.delete("/{payment_id}", response_model=schema.Payment)
def delete(payment_id: int, db: Session = Depends(get_db)):
    deleted = controller.delete(db=db, payment_id=payment_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Payment not found!")
    return deleted