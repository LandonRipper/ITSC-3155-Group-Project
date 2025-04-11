from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich

class CustomerBase(BaseModel):
    name: str
    email: str
    phone_number: str
    address: str

class CustomerCreate(CustomerBase):
    pass

class CustomerRead(CustomerBase):
    id: int
    class Config:
        orm_mode = True