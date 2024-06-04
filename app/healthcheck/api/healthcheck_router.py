from fastapi import APIRouter

from app.healthcheck.api.v1.healthcheck_api import healthcheck_v1_router

healthcheck_router = APIRouter()

healthcheck_router.include_router(
    healthcheck_v1_router,
    prefix="/healthcheck",
    tags=["Healthcheck"]
)
