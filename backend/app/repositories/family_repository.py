from sqlalchemy.orm import Session
from app.models.family_model import Family

# Crear familia
def create_family(db: Session, family_data):
    new_family = Family(**family_data)

    db.add(new_family)
    db.commit()
    db.refresh(new_family)

    return new_family

# Buscar familia por código de invitación
def get_family_by_code(db: Session, code: str):
    return db.query(Family).filter(Family.invite_code == code).first()