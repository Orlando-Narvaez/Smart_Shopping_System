from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from app.database.base import Base

# Modelo para la tabla de listas de compras
class ShoppingList(Base):
    __tablename__ = "shopping_lists"

    id = Column(Integer, primary_key=True, index=True)

    family_id = Column(Integer, ForeignKey("families.id"))
    status = Column(String(20), default="active")

    created_at = Column(TIMESTAMP, server_default=text("NOW()"))