from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.family_member_schema import JoinFamilyRequest, FamilyMemberResponse
from app.services import family_member_service

router = APIRouter(prefix="/family-members", tags=["Family Members"])

# conexión a la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# endpoint para unirse a una familia usando código de invitación
@router.post("/join", response_model=FamilyMemberResponse)
def join_family(request: JoinFamilyRequest, db: Session = Depends(get_db)):
    return family_member_service.join_family(
        db,
        request.user_id,
        request.invite_code
    )

# endpoint para obtener miembros de una familias
@router.get("/family/{family_id}", response_model=list[FamilyMemberResponse])
def get_members(family_id: int, db: Session = Depends(get_db)):
    return family_member_service.get_family_members(db, family_id)