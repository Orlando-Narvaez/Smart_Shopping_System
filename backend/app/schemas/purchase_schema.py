from pydantic import BaseModel
from datetime import datetime

class PurchaseCreate(BaseModel):
    family_id: int
    total_amount: float

class PurchaseResponse(BaseModel):
    id: int
    family_id: int
    date: datetime
    total_amount: float

    class Config:
        from_attributes = True