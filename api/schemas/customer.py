from typing import Optional
from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    email: str
    phone_number: str
    address: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

class CustomerRead(CustomerBase):
    id: int
    class Config:
        orm_mode = True

class Customer(BaseModel):
    name: str
    email: str
    phone_number: str
    address: str

    class Config:
        orm_mode = True

