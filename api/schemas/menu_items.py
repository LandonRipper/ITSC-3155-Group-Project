from typing import Optional
from pydantic import BaseModel


class MenuItemBase(BaseModel):
    item_name: str
    price: float
    calories: Optional[int] = None
    order_category: Optional[str] = None


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    item_name: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    order_category: Optional[str] = None


class MenuItem(MenuItemBase):
    id: int

    class Config:
        orm_mode = True
