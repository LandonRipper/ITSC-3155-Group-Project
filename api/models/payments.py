from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from .orders import Order
from ..dependencies.database import Base
#
class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    order_detail_id = Column(Integer, ForeignKey("order_details.id"), nullable=False)
    card_info = Column(String(100), nullable=False)
    transaction_status = Column(String(50), nullable=False)
    payment_type = Column(String(50), nullable=False)
    payment_amount = Column(DECIMAL, nullable=False)

    order = relationship("Order", back_populates="payment")
    order_detail = relationship("OrderDetail", back_populates="payment")