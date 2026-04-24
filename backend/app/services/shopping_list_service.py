from fastapi import HTTPException
from app.repositories import shopping_list_repository, family_member_repository


def create_list(db, family_id: int, user_id: int):

    # validar que pertenece a la familia
    membership = family_member_repository.get_membership(
        db, user_id, family_id
    )

    if not membership:
        raise HTTPException(
            status_code=403,
            detail="No perteneces a esta familia"
        )

    # validar que no exista una lista activa
    existing = shopping_list_repository.get_active_list(db, family_id)

    if existing:
        return existing  # reutilizamos la lista

    data = {
        "family_id": family_id,
        "status": "active"
    }

    return shopping_list_repository.create_list(db, data)