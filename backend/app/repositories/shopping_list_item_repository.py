from sqlalchemy.orm import Session
from app.models.shopping_list_item_model import ShoppingListItem


def create_item(db: Session, data):
    item = ShoppingListItem(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_items_by_list(db: Session, shopping_list_id: int):
    return db.query(ShoppingListItem).filter(
        ShoppingListItem.shopping_list_id == shopping_list_id
    ).all()


def update_item_status(db: Session, item_id: int, status: bool):
    item = db.query(ShoppingListItem).filter(
        ShoppingListItem.id == item_id
    ).first()

    if item:
        item.is_purchased = status
        db.commit()
        db.refresh(item)

    return item 