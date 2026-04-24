from sqlalchemy import Column, Integer, ForeignKey, Float, TIMESTAMP, text
from app.database.base import Base

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    family_id = Column(Integer, ForeignKey("families.id"))
    date = Column(TIMESTAMP, server_default=text("NOW()"))
    total_amount = Column(Float)