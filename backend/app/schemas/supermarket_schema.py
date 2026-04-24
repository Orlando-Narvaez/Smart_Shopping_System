from pydantic import BaseModel

class SupermarketCreate(BaseModel):
    name: str

class SupermarketResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True