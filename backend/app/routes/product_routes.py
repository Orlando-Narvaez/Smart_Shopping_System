from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.services import product_service
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product.dict())

@router.get("/", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return product_service.get_products(db)