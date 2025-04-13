from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse

from app.domain.enums import api_status
from app.domain.responses.api_response import APIResponse


class AuthException(HTTPException):
    def __init__(self, detail):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail
        )


async def auth_exception_handler(request: Request, ex: AuthException):
    api_response = APIResponse(
        service_status=api_status.FAIL,
        status_code=ex.status_code,
        data=ex.detail
    )
    return JSONResponse(
        content=api_response.model_dump(),
        status_code=ex.status_code
    )
