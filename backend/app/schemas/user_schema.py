from pydantic import BaseModel, EmailStr
from datetime import datetime

# Datos que envía el cliente (crear usuario)
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# Datos que devuelve la API
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True