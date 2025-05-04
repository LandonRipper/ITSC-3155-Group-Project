from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .order_details import OrderDetail
from .customer import Customer



class OrderBase(BaseModel):
    description: Optional[str] = None


class OrderCreate(OrderBase):
    customer_name: str
    description: Optional[str] = None

class OrderStatusUpdate(BaseModel):
    status_of_order: str
class AccountOrderCreate(OrderBase):
    email: str
    description: Optional[str] = None

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    status_of_order: str
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None
    customer: Optional[Customer]

    class ConfigDict:
        from_attributes = True
