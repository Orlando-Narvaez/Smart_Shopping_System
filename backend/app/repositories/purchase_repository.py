from sqlalchemy.orm import Session
from app.models.purchase_model import Purchase

def create_purchase(db: Session, data):
    new_purchase = Purchase(**data.dict())

    db.add(new_purchase)
    db.commit()
    db.refresh(new_purchase)

    return new_purchase