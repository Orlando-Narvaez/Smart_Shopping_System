from sqlalchemy.orm import Session
from app.models.user_model import User


# Crear usuario
def create_user(db: Session, user_data):
    new_user = User(**user_data.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Buscar usuario por email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()