# app/schemas/product.py

from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    category: str
    type: str
    description: Optional[str] = None
    price_per_gram: float
    rating: Optional[float] = 0.0
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    pass  # same as base while creating

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
