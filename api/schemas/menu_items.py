from typing import Optional
from pydantic import BaseModel
from decimal import Decimal


class MenuItemBase(BaseModel):
    item_name: str
    price: Decimal
    calories: Optional[int] = None
    order_category: Optional[str] = None


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    item_name: Optional[str] = None
    price: Optional[Decimal] = None
    calories: Optional[int] = None
    order_category: Optional[str] = None


class MenuItem(MenuItemBase):
    id: int

    class ConfigDict:
        from_attributes = True

