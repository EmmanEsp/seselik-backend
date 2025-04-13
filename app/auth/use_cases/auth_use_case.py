from fastapi import Depends

from app.auth.services.auth_service import AuthService
from app.auth.domain.requests.login_request import LoginRequest
from app.auth.domain.responses.login_response import LoginResponse

class AuthUseCase:

    def __init__(self, auth_service: AuthService = Depends()) -> None:
        self.auth_service = auth_service

    def login(self, login_request: LoginRequest) -> LoginResponse:
        return LoginResponse(
            token=self.auth_service.login(login_request=login_request)
        )
