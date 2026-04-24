from sqlalchemy.orm import Session
from app.repositories import purchase_repository

def create_purchase(db: Session, data):
    return purchase_repository.create_purchase(db, data)