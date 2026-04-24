from sqlalchemy.orm import Session
from app.models.brand_model import Brand

def create_brand(db: Session, brand_data):
    brand = Brand(**brand_data)
    db.add(brand)
    db.commit()
    db.refresh(brand)
    return brand

def get_brands(db: Session):
    return db.query(Brand).all()