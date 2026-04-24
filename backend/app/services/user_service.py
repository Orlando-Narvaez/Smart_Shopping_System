from sqlalchemy.orm import Session
from app.repositories import user_repository
from app.core.security import hash_password

# Servicio para manejar la lógica de usuarios
def create_user(db: Session, user_data):
    # Verificar si ya existe el usuario
    existing_user = user_repository.get_user_by_email(db, user_data.email)

    if existing_user:
        raise Exception("El usuario ya existe")
    
    # hashear contraseña
    user_data.password = hash_password(user_data.password)

    #  Crear usuario
    return user_repository.create_user(db, user_data)