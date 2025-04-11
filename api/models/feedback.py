from sqlalchemy import Column, ForeignKey, Integer, String, Text, CheckConstraint
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Feedback(Base):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    reviewer_name = Column(String(100), nullable=True)
    rating = Column(Integer, nullable=False)
    review = Column(Text, nullable=True)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)

    item = relationship("MenuItems", back_populates="feedback")

    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
    )


