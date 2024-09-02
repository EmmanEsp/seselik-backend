from fastapi import APIRouter

from app.product.api.v1.product_controller import product_v1_router
from app.product.api.v1.product_status_controller import product_status_v1_router

product_router = APIRouter()

product_router.include_router(
    product_v1_router,
    prefix="/product",
    tags=["Product"]
)

product_router.include_router(
    product_status_v1_router,
    prefix="/product-status",
    tags=["Product Status"]
)
