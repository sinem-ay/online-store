from models import Product
from schemas.product import Product, ProductCreate
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException

from database.database_singleton import get_db

app = APIRouter()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/products")
def get_products(
    db_session: Session = Depends(get_db),
):
    print("start")
    products = db_session.query(Product).all()
    print(products)
    print(type(products))
    return products


@app.post("/product", response_model=ProductCreate)
async def create_product(
    product: Product,
    db_session: Session = Depends(get_db),
):
    db_product = (
        db_session.query(Product)
        .filter(Product.product_name == product.product_name)
        .first()
    )

    if db_product is not None:
        raise HTTPException(status_code=400, detail="Product already exists")

    new_product = Product(product_name=product.product_name, price=product.price)

    db_session.add(new_product)
    db_session.commit()
