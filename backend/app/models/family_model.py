from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from app.database.base import Base

# Modelo de familia
class Family(Base):
    __tablename__ = "families"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    invite_code = Column(String(10), unique=True, index=True)
    created_at = Column(TIMESTAMP, server_default=text("NOW()"))