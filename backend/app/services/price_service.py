from sqlalchemy.orm import Session
from app.repositories import price_repository

def create_price(db: Session, data):
    return price_repository.create_price(db, data)