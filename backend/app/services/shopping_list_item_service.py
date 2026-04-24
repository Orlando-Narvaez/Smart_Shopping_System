from fastapi import HTTPException
from app.repositories import shopping_list_item_repository


def add_item(db, data):
    return shopping_list_item_repository.create_item(db, data)


def get_items(db, shopping_list_id: int):
    return shopping_list_item_repository.get_items_by_list(db, shopping_list_id)


def mark_as_purchased(db, item_id: int):
    item = shopping_list_item_repository.update_item_status(db, item_id, True)

    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")

    return item