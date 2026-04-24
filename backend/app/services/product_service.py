from app.repositories import product_repository

def create_product(db, product_data):
    return product_repository.create_product(db, product_data)

def get_products(db):
    return product_repository.get_products(db)