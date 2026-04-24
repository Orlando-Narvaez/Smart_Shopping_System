from sqlalchemy.orm import Session
from app.models.purchase_item_model import PurchaseItem

def create_purchase_item(db: Session, data):
    new_item = PurchaseItem(**data.dict())

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item