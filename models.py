import uuid

import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    product_id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_name = sa.Column(sa.String(100), nullable=False)
    price = sa.Column(sa.Float, nullable=False)


class Provider(Base):
    __tablename__ = 'providers'

    provider_id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = sa.Column(ForeignKey('products.product_id'), nullable=False)
    quantity = sa.Column(sa.Integer, nullable=False)
    total_price = sa.Column(sa.Float, nullable=False)  # quantity * products.price
    date = sa.Column(sa.DateTime, server_default=func.now())
    product = relationship(Product)

    def __repr__(self):
        return f'id: {self.product_id}, name: {self.product.name}'


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_name = sa.Column(sa.String(100))
    customer_email = sa.Column(sa.String(100), nullable=False)
