from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .orders import Order


class PromotionBase(BaseModel):
    restuarant_id: int
    description: Optional[str] = "Current Promotions"


class PromoCreate(PromotionBase):
    promo_id = int



class PromoUpdate(BaseModel):
    promo_id : Optional[int] = None
    description: Optional[str] = None
    promotion_name: Optional[str] = None


class PromoDelete(PromotionBase):
    id: int
    promo_id: int

class PromoRead(PromotionBase):


    class ConfigDict:
        from_attributes = True
