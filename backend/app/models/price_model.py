from sqlalchemy import Column, Integer, ForeignKey, Float, TIMESTAMP, String, text
from app.database.base import Base

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)
    product_variant_id = Column(Integer, ForeignKey("product_variants.id"))
    supermarket_id = Column(Integer, ForeignKey("supermarkets.id"))
    price = Column(Float)
    quantity = Column(Float)
    unit = Column(String(20))
    updated_at = Column(TIMESTAMP, server_default=text("NOW()"), onupdate=text("NOW()"))