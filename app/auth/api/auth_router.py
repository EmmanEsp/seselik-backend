from fastapi import APIRouter

from app.auth.api.v1.auth_controller import auth_v1_router

auth_router = APIRouter()


auth_router.include_router(auth_v1_router, prefix="/v1/auth", tags=["Auth"])
