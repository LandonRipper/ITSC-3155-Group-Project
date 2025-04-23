from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotion_id = Column(Integer, ForeignKey("promotions.id"))
    promotion_name = Column(String(50), unique=True, nullable=False)
    exp_date = Column(Integer, nullable=False)
    

    