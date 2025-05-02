from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    card_info: str
    transaction_status: str
    payment_type: str
    order_detail_id: int

class PaymentCreate(PaymentBase):
    order_id: int
    order_detail_id: int

class PaymentRead(PaymentBase):
    id: int
    order_id: int

    class ConfigDict:
        orm_mode = True

class PaymentUpdate(BaseModel):
    card_info: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None

class Payment(PaymentBase):
    id: int
    order_id: int
    class ConfigDict:
        orm_mode = True
