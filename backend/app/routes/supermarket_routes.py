from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.supermarket_schema import SupermarketCreate, SupermarketResponse
from app.services import supermarket_service

router = APIRouter(prefix="/supermarkets", tags=["Supermarkets"])

@router.post("/", response_model=SupermarketResponse)
def create_supermarket(supermarket: SupermarketCreate, db: Session = Depends(get_db)):
    return supermarket_service.create_supermarket(db, supermarket)