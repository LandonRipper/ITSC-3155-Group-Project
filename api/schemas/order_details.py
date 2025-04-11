from typing import Optional
from pydantic import BaseModel
from .menu_items import MenuItem


class OrderDetailBase(BaseModel):
    quantity: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    item_id: int


class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    item_id: Optional[int] = None
    quantity: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    item: Optional[MenuItem] = None

    class Config:
        orm_mode = True
