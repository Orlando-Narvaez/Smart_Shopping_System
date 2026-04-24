from sqlalchemy.orm import Session
from app.repositories import supermarket_repository

def create_supermarket(db: Session, data):
    return supermarket_repository.create_supermarket(db, data)