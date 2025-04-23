from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, Date
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotion_name = Column(String(50), unique=True, nullable=False)
    exp_date = Column(Date, nullable=False)
    

    