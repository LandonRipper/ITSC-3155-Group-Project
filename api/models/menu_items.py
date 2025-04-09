from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class MenuItems(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item_name = Column(String(100), unique=True, nullable=True)
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    calories = Column(Integer, minimum=1)
    order_category = Column(String(100), nullable=True)

    recipes = relationship("Recipe", back_populates="item")
    #order_details = relationship("OrderDetail", back_populates="item")

