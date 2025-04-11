from typing import Optional
from pydantic import BaseModel, Field
from .menu_items import MenuItem


class FeedbackBase(BaseModel):
    reviewer_name: Optional[str] = None
    rating: int = Field(..., ge=1, le=5, description="Rating must be between 1 and 5")
    review: Optional[str] = None


class FeedbackCreate(FeedbackBase):
    menu_item_id: int


class FeedbackUpdate(BaseModel):
    reviewer_name: Optional[str] = None
    rating: Optional[int] = Field(None, ge=1, le=5)
    review: Optional[str] = None
    menu_item_id: Optional[int] = None


class Feedback(FeedbackBase):
    id: int
    menu_item_id: int
    item: Optional[MenuItem] = None

    class Config:
        orm_mode = True
