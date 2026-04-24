from sqlalchemy.orm import Session
from app.repositories import family_member_repository, family_repository
from fastapi import HTTPException

# Servicio para manejar la lógica de familias y miembros de familia
def join_family(db: Session, user_id: int, invite_code: str):
    # Buscar familia por código de invitación
    family = family_repository.get_family_by_code(db, invite_code)

    # Si no se encuentra la familia, lanzar error
    if not family:
        raise HTTPException(
            status_code=404,
            detail="Código inválido"
        )
    
    # Verificar si el usuario ya es miembro de la familia
    existing = family_member_repository.get_membership(
        db, user_id, family.id
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="El usuario ya pertenece a esta familia"
        )

    # Crear miembro de familia
    data = {
        "user_id": user_id,
        "family_id": family.id,
        "role": "member"
    }

    # Agregar usuario a la familia
    return family_member_repository.create_family_member(db, data)

# Obtener miembros de una familia
def get_family_members(db: Session, family_id: int):
    return family_member_repository.get_members_by_family(db, family_id)