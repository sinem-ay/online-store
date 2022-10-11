from pydantic import BaseModel
from pydantic.types import UUID4

from typing import Optional


class Product(BaseModel):
    product_id: UUID4
    product_name: str
    price: float

    class Config:
        orm_mode = True


class ProductCreate(Product):
    product_name: str
    price: float

    class Config:
        orm_mode = True
