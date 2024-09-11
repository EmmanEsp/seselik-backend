from fastapi import HTTPException, status, Request
from fastapi.responses import JSONResponse 

from app.domain.responses.api_response import APIResponse
from app.domain.enums import api_status


class ServiceException(HTTPException):
    def __init__(self, detail):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail
        )


async def service_exception_handler(request: Request, ex: ServiceException):
    api_response = APIResponse(
        service_status=api_status.ERROR,
        status_code=ex.status_code,
        data=ex.detail)
    return JSONResponse(content=api_response.model_dump(), status_code=ex.status_code)
