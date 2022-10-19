from uuid import UUID
from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from schemas.product import ProductBase
from models import Product, Base
from database.database_fast import SessionLocal, engine

from database.database_fast import get_db

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get('/product/{product_id}', response_model=ProductBase)
async def read_product(
        product_id: UUID, db: Session = Depends(get_db)
) -> List[Product]:
    db_product = db.query(Product).filter(product_id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail='Product not found')
    return db_product


@router.get('/products', response_model=List[ProductBase])
async def read_products(
        skip: int = 0, limit: int = 0, db: Session = Depends(get_db)
) -> List[Product]:
    products = db.query(Product).offset(skip).limit(limit).all()
    return products


@router.post('/product', response_model=ProductBase)
async def create_product(
        product: ProductBase, db: Session = Depends(get_db)
):
    db_product = db.query(Product).filter(Product.product_id == product.product_id).first()
    if db_product is not None:
        raise HTTPException(status_code=400, detail='Product already exists')

    new_product = Product(
        product_id=product.product_id,
        product_name=product.product_name,
        price=product.price
    )
    db.add(new_product)
    db.commit()
    return new_product
