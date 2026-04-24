from app.repositories import product_variant_repository

def create_variant(db, data):
    return product_variant_repository.create_variant(db, data)

def get_variants(db):
    return product_variant_repository.get_variants(db)