from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.purchase_item_schema import PurchaseItemCreate, PurchaseItemResponse
from app.services import purchase_item_service

router = APIRouter(prefix="/purchase-items", tags=["Purchase Items"])

@router.post("/", response_model=PurchaseItemResponse)
def create_purchase_item(item: PurchaseItemCreate, db: Session = Depends(get_db)):
    return purchase_item_service.create_purchase_item(db, item)