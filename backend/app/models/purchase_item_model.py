from sqlalchemy import Column, Integer, ForeignKey, Float
from app.database.base import Base

class PurchaseItem(Base):
    __tablename__ = "purchase_items"

    id = Column(Integer, primary_key=True, index=True)
    purchase_id = Column(Integer, ForeignKey("purchases.id"))
    product_variant_id = Column(Integer, ForeignKey("product_variants.id"))
    quantity = Column(Float)
    price = Column(Float)