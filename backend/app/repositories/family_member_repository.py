from sqlalchemy.orm import Session
from app.models.family_member_model import FamilyMember

# Crear miembro de familia
def create_family_member(db: Session, data):
    new_member = FamilyMember(**data)

    db.add(new_member)
    db.commit()
    db.refresh(new_member)

    return new_member

# Buscar miembros por ID de familia
def get_members_by_family(db: Session, family_id: int):
    return db.query(FamilyMember).filter(FamilyMember.family_id == family_id).all()

# Verificar si un usuario ya es miembro de una familia
def get_membership(db: Session, user_id: int, family_id: int):
    return db.query(FamilyMember).filter(
        FamilyMember.user_id == user_id,
        FamilyMember.family_id == family_id
    ).first()