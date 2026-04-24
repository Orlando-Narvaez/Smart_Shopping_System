from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.price_schema import PriceCreate, PriceResponse
from app.services import price_service

router = APIRouter(prefix="/prices", tags=["Prices"])

@router.post("/", response_model=PriceResponse)
def create_price(price: PriceCreate, db: Session = Depends(get_db)):
    return price_service.create_price(db, price)