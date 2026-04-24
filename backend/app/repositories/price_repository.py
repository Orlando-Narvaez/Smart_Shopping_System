from sqlalchemy.orm import Session
from app.models.price_model import Price

def create_price(db: Session, data):
    new_price = Price(**data.dict())

    db.add(new_price)
    db.commit()
    db.refresh(new_price)

    return new_price