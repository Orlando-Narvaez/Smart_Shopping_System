from app.repositories import brand_repository

def create_brand(db, brand_data):
    return brand_repository.create_brand(db, brand_data)

def get_brands(db):
    return brand_repository.get_brands(db)