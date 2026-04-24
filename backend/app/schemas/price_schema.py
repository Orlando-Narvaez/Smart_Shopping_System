from pydantic import BaseModel
from datetime import datetime

class PriceCreate(BaseModel):
    product_variant_id: int
    supermarket_id: int
    price: float
    quantity: float
    unit: str

class PriceResponse(BaseModel):
    id: int
    product_variant_id: int
    supermarket_id: int
    price: float
    quantity: float
    unit: str
    updated_at: datetime

    class Config:
        from_attributes = True