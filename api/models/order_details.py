from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    price = Column(DECIMAL(6,2), nullable=False)
    quantity = Column(Integer, nullable=False, index=True)
    type_of_order = Column(String(300))

    item = relationship("MenuItem", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")
    payment = relationship("Payment", back_populates="order_detail", uselist=False)


