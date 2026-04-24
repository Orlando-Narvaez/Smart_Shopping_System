from pydantic import BaseModel

class ProductVariantBase(BaseModel):
    product_id: int
    brand_id: int
    image_url: str | None = None

class ProductVariantCreate(ProductVariantBase):
    pass

class ProductVariantResponse(ProductVariantBase):
    id: int

    class Config:
        from_attributes = True