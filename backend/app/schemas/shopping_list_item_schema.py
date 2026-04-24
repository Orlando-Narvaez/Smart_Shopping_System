from pydantic import BaseModel

class ShoppingListItemCreate(BaseModel):
    shopping_list_id: int
    product_variant_id: int
    quantity: int
    unit: str


class ShoppingListItemResponse(BaseModel):
    id: int
    shopping_list_id: int
    product_variant_id: int
    quantity: int
    unit: str
    is_purchased: bool

    class Config:
        from_attributes = True