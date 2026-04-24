from sqlalchemy.orm import Session
from app.repositories import family_repository
from app.utils.code_generator import generate_invite_code

# Servicio para manejar la lógica de familias
def create_family(db: Session, family_data):
    # Generar código de invitación único
    invite_code = generate_invite_code()

    # Verificar que el código no exista
    new_family_data = {
        "name": family_data.name,
        "invite_code": invite_code
    }

    # Crear familia
    return family_repository.create_family(db, new_family_data)