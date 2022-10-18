from pydantic import BaseModel
from pydantic.types import UUID4


class ProductBase(BaseModel):
    product_id: UUID4
    product_name: str
    price: float

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    product_name: str
    price: float

    class Config:
        orm_mode = True
