from typing import Optional
from pydantic import BaseModel
from .menu_items import MenuItem


class OrderDetailBase(BaseModel):
    quantity: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    item_id: int
    type_of_order: str

class OrderDetailUpdate(BaseModel):
    quantity: Optional[int] = None

class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    item: Optional[MenuItem] = None
    type_of_order: str


    class Config:
        orm_mode = True
