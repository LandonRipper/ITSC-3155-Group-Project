from .customer import Customer
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, Date
from sqlalchemy.orm import relationship
from datetime import date
from ..dependencies.database import Base
import random


def generate_tracking_number():
    return random.randint(100000, 999999)  # Adjust range as needed

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_date = Column(Date, nullable=False, default=date.today)
    description = Column(String(300))
    tracking_number = Column(Integer, unique=True, nullable=False, default=generate_tracking_number)
    status_of_order = Column(String(300),default="In Progress")

    customer_id = Column(Integer, ForeignKey("customers.id"),nullable=True)
    customer = relationship("Customer", back_populates="orders")

    order_details = relationship("OrderDetail", back_populates="order")
    payment = relationship("Payment", back_populates="order", uselist=False)