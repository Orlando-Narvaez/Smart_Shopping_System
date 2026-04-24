from sqlalchemy.orm import Session
from app.repositories import purchase_item_repository

def create_purchase_item(db: Session, data):
    return purchase_item_repository.create_purchase_item(db, data)