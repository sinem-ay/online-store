from typing import Optional, List
from sqlalchemy.orm import Session
import sqlalchemy.exc

from uuid import UUID
from models import Product
from schemas.product import ProductBase, ProductCreate, ProductUpdate


def get_products(
    db: Session, skip: Optional[int] = 0, limit: Optional[int] = 100
) -> List[Product]:
    if skip == 0 and limit == 0:
        return db.query(Product).all()
    return db.query(Product).offset(skip).limit(limit).all()


def get_product(db: Session, product_name: str) -> Product:
    return db.query(Product).filter(Product.product_name == product_name).first()


def create_product(db: Session, product: ProductCreate) -> Product:
    db_product = Product(**product.dict())
    db.add(db_product)
    try:
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
    except sqlalchemy.exc.IntegrityError as e:
        db.rollback()
    return db_product


def update_product(db: Session, product_id: UUID, product: ProductUpdate) -> Product:
    db_obj = db.query(Product).filter(Product.product_id == product_id).first()
    for name, value in product.dict(exclude_unset=True).items():
        setattr(db_obj, name, value)
    db.commit()
    return db_obj


def delete_product(db: Session, product_id: UUID):
    db_delete = db.query(Product).filter(Product.product_id == product_id).first()
    db.delete(db_delete)
    db.commit()
    return db_delete
