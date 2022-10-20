from pydantic import BaseModel
from pydantic import UUID4, Field

from uuid import uuid4


class ProductBase(BaseModel):
    product_id: UUID4 = Field(default_factory=uuid4)
    product_name: str = Field(default='', max_length=100)
    price: float

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    product_name: str

    class Config:
        orm_mode = True
