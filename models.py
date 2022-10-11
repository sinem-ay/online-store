import uuid

import sqlalchemy as db
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    product_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Provider(Base):
    __tablename__ = 'providers'

    provider_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = db.Column(ForeignKey('products.product_id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)  # quantity * products.price
    date = db.Column(db.DateTime, server_default=func.now())


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_name = db.Column(db.String(100))
    customer_email = db.Column(db.String(100), nullable=False)