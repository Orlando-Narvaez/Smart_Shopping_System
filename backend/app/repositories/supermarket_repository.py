from sqlalchemy.orm import Session
from app.models.supermarket_model import Supermarket

def create_supermarket(db: Session, data):
    new_supermarket = Supermarket(**data.dict())

    db.add(new_supermarket)
    db.commit()
    db.refresh(new_supermarket)

    return new_supermarket