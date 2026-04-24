from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services import shopping_list_service

router = APIRouter(prefix="/shopping-lists", tags=["Shopping Lists"])


@router.post("/{family_id}")
def create_or_get_list(
    family_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):
    return shopping_list_service.create_list(db, family_id, user_id)