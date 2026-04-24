from pydantic import BaseModel

class PurchaseItemCreate(BaseModel):
    purchase_id: int
    product_variant_id: int
    quantity: float
    price: float

class PurchaseItemResponse(BaseModel):
    id: int
    purchase_id: int
    product_variant_id: int
    quantity: float
    price: float

    class Config:
        from_attributes = True