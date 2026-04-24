from sqlalchemy.orm import Session
from app.models.shopping_list_model import ShoppingList


def create_list(db: Session, data):
    new_list = ShoppingList(**data)
    db.add(new_list)
    db.commit()
    db.refresh(new_list)
    return new_list


def get_active_list(db: Session, family_id: int):
    return db.query(ShoppingList).filter(
        ShoppingList.family_id == family_id,
        ShoppingList.status == "active"
    ).first()