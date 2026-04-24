from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.shopping_list_item_schema import (
    ShoppingListItemCreate,
    ShoppingListItemResponse
)
from app.services import shopping_list_item_service

router = APIRouter(prefix="/shopping-list-items", tags=["Shopping List Items"])


@router.post("/", response_model=ShoppingListItemResponse)
def add_item(data: ShoppingListItemCreate, db: Session = Depends(get_db)):
    return shopping_list_item_service.add_item(db, data.dict())


@router.get("/{shopping_list_id}", response_model=list[ShoppingListItemResponse])
def get_items(shopping_list_id: int, db: Session = Depends(get_db)):
    return shopping_list_item_service.get_items(db, shopping_list_id)


@router.patch("/{item_id}/purchase", response_model=ShoppingListItemResponse)
def mark_purchased(item_id: int, db: Session = Depends(get_db)):
    return shopping_list_item_service.mark_as_purchased(db, item_id)