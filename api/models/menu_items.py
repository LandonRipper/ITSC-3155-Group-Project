from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class MenuItems(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item_name = Column(String(100), unique=True, nullable=False)
    price = Column(DECIMAL(6, 2), nullable=False, server_default='0.00')
    calories = Column(Integer, nullable=True)
    order_category = Column(String(100), nullable=True)

    recipes = relationship("Recipe", back_populates="item")
    order_details = relationship("OrderDetail", back_populates="item")

