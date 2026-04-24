from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Supermarket(Base):
    __tablename__ = "supermarkets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))