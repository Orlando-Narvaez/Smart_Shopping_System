from sqlalchemy import Column, Integer, ForeignKey, Boolean, String
from app.database.base import Base

class ShoppingListItem(Base):
    __tablename__ = "shopping_list_items"

    id = Column(Integer, primary_key=True, index=True)

    shopping_list_id = Column(Integer, ForeignKey("shopping_lists.id"))
    product_variant_id = Column(Integer, ForeignKey("product_variants.id"))

    quantity = Column(Integer)
    unit = Column(String(20))

    is_purchased = Column(Boolean, default=False)