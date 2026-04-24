from pydantic import BaseModel
from datetime import datetime

# Datos que envía el cliente (crear familia)
class FamilyCreate(BaseModel):
    name: str

# Datos que devuelve la API
class FamilyResponse(BaseModel):
    id: int
    name: str
    invite_code: str
    created_at: datetime

    class Config:
        from_attributes = True