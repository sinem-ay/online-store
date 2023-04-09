import uuid
from datetime import datetime
from typing import Optional, List

from sqlalchemy import Column, String, Float, Integer, DateTime
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint

from database.database_singleton import Base


class Product(Base):
    __tablename__ = "product"

    product_id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_name: Mapped[str] = mapped_column(String(256), nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)
    product_country: Mapped[Optional[str]]
    time_created = mapped_column(DateTime(timezone=True), server_default=func.now())
    time_updated = mapped_column(DateTime(timezone=True), onupdate=func.now())


class Provider(Base):
    __tablename__ = "provider"

    provider_id = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)
    provide_date: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    time_created = mapped_column(DateTime(timezone=True), server_default=func.now())
    time_updated = mapped_column(DateTime(timezone=True), onupdate=func.now())


class ProductProviderAssociation(Base):
    __tablename__ = "product_provider_association"

    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("product.product_id", ondelete="CASCADE"),
        primary_key=True,
        default=uuid.uuid4,
    )
    provider_id = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("provider.provider_id", ondelete="CASCADE"),
        primary_key=True,
        default=uuid.uuid4,
    )
    __table_args__ = (
        UniqueConstraint(
            "product_id",
            "provider_id",
            name="uix_product_provider_association",
        ),
    )
