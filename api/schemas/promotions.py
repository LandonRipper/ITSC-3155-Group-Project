from pydantic import BaseModel, condecimal, constr
from datetime import date
from typing import Optional


class PromotionBase(BaseModel):
    promotion_name: constr(max_length=50)
    discount: condecimal(max_digits=2, decimal_places=2, ge=0)
    exp_date: date


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    promotion_name: Optional[constr(max_length=50)] = None
    discount: Optional[condecimal(max_digits=2, decimal_places=2, ge=0)] = None
    exp_date: Optional[date] = None


class Promotion(PromotionBase):
    id: int

    class Config:
        orm_mode = True
