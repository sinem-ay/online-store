from uuid import UUID
from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from schemas.product import ProductBase, ProductCreate, ProductUpdate
from models import Product, Base
from database.database_fast import SessionLocal, engine
from api import crud_product

from database.database_fast import get_db

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get("/product/{product_name}", response_model=ProductBase)
async def read_product(product_name: str, db: Session = Depends(get_db)) -> Product:
    db_product = crud_product.get_product(db, product_name=product_name)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.get("/products", response_model=List[ProductBase])
async def read_products(
    skip: int = 0, limit: int = 0, db: Session = Depends(get_db)
) -> List[Product]:
    products = crud_product.get_products(db, skip, limit)
    return products


@router.post("/product", response_model=ProductBase)
async def create_product(
    product: ProductCreate, db: Session = Depends(get_db)
) -> Product:
    db_product = crud_product.create_product(db, product=product)
    if not db_product:
        raise HTTPException(status_code=400, detail="Product already exists")
    return db_product


@router.put("/product/{product_id}", response_model=ProductBase)
async def update_product(
    product_id: UUID, product: ProductUpdate, db: Session = Depends(get_db)
):
    db_product = crud_product.update_product(db, product_id, product=product)
    return db_product


@router.delete("/product/{product_id}", response_model=ProductBase)
async def delete_product(product_id: UUID, db: Session = Depends(get_db)):
    db_product = crud_product.delete_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
