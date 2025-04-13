from fastapi import APIRouter, Depends, status

from app.auth.domain.requests.login_request import LoginRequest
from app.auth.domain.responses.login_response import LoginResponse
from app.auth.use_cases.auth_use_case import AuthUseCase
from app.domain.enums import api_status
from app.domain.responses.api_response import APIResponse

auth_v1_router = APIRouter()


@auth_v1_router.post(
    "/login",
    response_model=APIResponse[LoginResponse],
    status_code=status.HTTP_200_OK,
)
def login(login_request: LoginRequest, use_case: AuthUseCase = Depends()):
    """Login a user"""
    use_case.login(login_request=login_request)
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_200_OK,
        data=use_case.login(login_request=login_request),
    )
