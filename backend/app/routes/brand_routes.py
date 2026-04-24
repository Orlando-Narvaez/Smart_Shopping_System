from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database.connection import get_db
from app.schemas.brand_schema import BrandCreate, BrandResponse
from app.services import brand_service

router = APIRouter(prefix="/brands", tags=["Brands"])

@router.post("/", response_model=BrandResponse)
def create_brand(brand: BrandCreate, db: Session = Depends(get_db)):
    return brand_service.create_brand(db, brand.dict())

@router.get("/", response_model=List[BrandResponse])
def get_brands(db: Session = Depends(get_db)):
    return brand_service.get_brands(db)