from pydantic import BaseModel
from datetime import datetime

class ShoppingListCreate(BaseModel):
    family_id: int


class ShoppingListResponse(BaseModel):
    id: int
    family_id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True