from uuid import UUID
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from schemas.product import ProductBase, ProductCreate
from models import Product, Base
from database.database_fast import SessionLocal, engine

from api.crud_product import get_products, get_product
from database.database_fast import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/product/{product_id}', response_model=ProductBase)
def read_product(product_id: UUID, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail='Product not found')
    return db_product


@app.get('/products', response_model=List[ProductBase])
def read_products(skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    products = get_products(db, skip=skip, limit=limit)
    return products
