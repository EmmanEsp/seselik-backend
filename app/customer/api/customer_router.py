from fastapi import APIRouter

from app.customer.api.v1.customer_controller import customer_v1_router
from app.customer.api.v1.ship_address_controller import ship_address_v1_router

customer_router = APIRouter()


customer_router.include_router(
    customer_v1_router,
    prefix="/customer",
    tags=["Customer"]
)

customer_router.include_router(
    ship_address_v1_router,
    prefix="/ship-address",
    tags=["Ship Address"]
)
