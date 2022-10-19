from pydantic import BaseModel
from pydantic.types import UUID4

from datetime import datetime


class ProviderBase(BaseModel):
    provider_id: UUID4
    quantity: int
    total_price: float
    date: datetime


class ProviderCreate(ProviderBase):
    provider_id: UUID4
    product_id: UUID4
    quantity: int
    total_price: float
    date: datetime
