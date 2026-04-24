from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import get_db
from app.schemas.product_variant_schema import ProductVariantCreate, ProductVariantResponse
from app.services import product_variant_service

router = APIRouter(prefix="/product-variants", tags=["Product Variants"])

@router.post("/", response_model=ProductVariantResponse)
def create_variant(data: ProductVariantCreate, db: Session = Depends(get_db)):
    return product_variant_service.create_variant(db, data.dict())

@router.get("/", response_model=List[ProductVariantResponse])
def get_variants(db: Session = Depends(get_db)):
    return product_variant_service.get_variants(db)