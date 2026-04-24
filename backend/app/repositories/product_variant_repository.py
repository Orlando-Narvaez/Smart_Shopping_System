from sqlalchemy.orm import Session
from app.models.product_variant_model import ProductVariant

def create_variant(db: Session, data):
    variant = ProductVariant(**data)
    db.add(variant)
    db.commit()
    db.refresh(variant)
    return variant

def get_variants(db: Session):
    return db.query(ProductVariant).all()