from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.family_schema import FamilyCreate, FamilyResponse
from app.services import family_service

router = APIRouter(prefix="/families", tags=["Families"])

# conexión a la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# endpoint para crear familia
@router.post("/", response_model=FamilyResponse)
def create_family(family: FamilyCreate, db: Session = Depends(get_db)):
    return family_service.create_family(db, family)