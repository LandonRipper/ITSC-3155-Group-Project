from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .orders import Order



class PromotionBase(BaseModel):
    restaurant_name: str
    description: Optional[str] = "Current Promotions"



#Intended for the restaurant to create promotions
class PromoCreate(PromotionBase):
    pass


#Intended for the restaurant to update promos
class PromoUpdate(BaseModel):
    promo_name: Optional[str] = None
    promo_id : Optional[int] = None
    description: Optional[str] = None

class PromoDelete(BaseModel):
    pass

#
class Order(PromotionBase):
    id: int
    promotion_name: str
    promotion_id: int
    exp_date: datetime


    class ConfigDict:
        from_attributes = True
