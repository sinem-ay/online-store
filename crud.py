import models
import schemas
import session
import schemas
from sqlalchemy.orm import Session
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

app = APIRouter()


@app.get('/products', response_model=schemas.Product)
async def get_products(
        db_session: Session = Depends(session.get_session),
) -> List[models.Product]:
    return db_session.query(models.Product).all()


@app.post('/product', response_model=schemas.ProductCreate)
async def create_product(
        product: schemas.Product,
        db_session: Session = Depends(session.get_session),
):
    db_product = db_session.query(models.Product). \
        filter(models.Product.product_name == product.product_name).first()

    if db_product is not None:
        raise HTTPException(status_code=400, detail='Product already exists')

    new_product = models.Product(
        product_name=product.product_name,
        price=product.price
    )

    db_session.add(new_product)
    db_session.commit()