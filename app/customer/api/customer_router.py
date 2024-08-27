from fastapi import APIRouter

from app.customer.api.v1.customer_controller import customer_v1_router

customer_router = APIRouter()

customer_router.include_router(
    customer_v1_router,
    prefix="/customer",
    tags=["customer"]
)
