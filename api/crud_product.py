from typing import Optional
from sqlalchemy.orm import Session
import sqlalchemy.exc

from uuid import UUID
from models import Product
from schemas.product import ProductBase, ProductCreate


def get_products(db: Session, skip: Optional[int] = 0, limit: Optional[int] = 100):
    if skip == 0 and limit == 0:
        return db.query(Product).all()
    return db.query(Product).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: UUID):
    return db.query(Product).filter(Product.product_id == product_id).first()


def create_product(db: Session, product_id: UUID, product: ProductCreate):
    db.query(Product).filter(product.product_id == product_id).first()
    new_product = Product(
        product_id=product.product_id,
        product_name=product.product_name,
        price=product.price
    )
    db.add(new_product)
    db.commit()
    return new_product


def update_product(db: Session, product: ProductBase):
    db_obj = get_product(db, product_id=product.product_id)
    for column, value in product.dict(exclude_unset=True).items():
        setattr(db_obj, column, value)
    db.commit()
    return db_obj


