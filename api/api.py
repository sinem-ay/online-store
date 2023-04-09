from fastapi import APIRouter

from api.endpoints import product, provider

router = APIRouter()

router.include_router(product.router, tags=["product"])
router.include_router(provider.router, tags=["provider"])
