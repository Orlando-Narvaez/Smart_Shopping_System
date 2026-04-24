from pydantic import BaseModel
from datetime import datetime

# Datos que envía el cliente (unirse a familia)
class JoinFamilyRequest(BaseModel):
    user_id: int
    invite_code: str

# Datos que devuelve la API
class FamilyMemberResponse(BaseModel):
    id: int
    user_id: int
    family_id: int
    role: str
    joined_at: datetime

    class Config:
        from_attributes = True