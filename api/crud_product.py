from sqlalchemy.orm import Session

from uuid import UUID, uuid4
from models import Product


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: UUID):
    return db.query(Product).filter(product_id == product_id).first()
