from fastapi import HTTPException, status, Request
from fastapi.responses import JSONResponse 

from app.entities.responses.api_response import APIResponse
from app.entities.enums import api_status


class CustomerException(HTTPException):
    def __init__(self, detail):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )


async def customer_exception_handler(request: Request, ex: CustomerException):
    api_response = APIResponse(
        service_status=api_status.FAIL,
        status_code=ex.status_code,
        data=ex.detail)
    return JSONResponse(content=api_response.model_dump(), status_code=ex.status_code)
