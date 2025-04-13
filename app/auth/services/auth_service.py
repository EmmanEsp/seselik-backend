from fastapi import Depends
from sqlalchemy.orm import Session

from app.auth.domain.exceptions.auth_exception import AuthException
from app.auth.domain.requests.login_request import LoginRequest
from app.customer.domain.models.customer_model import CustomerModel
from app.infraestructure.database import get_db
from app.security.claims import Claims
from app.security.jwt import create_access_token
from app.security.password import verify_password
from app.security.roles_config import ROLE_PERMISSIONS


class AuthService:
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self._db = db

    def get_user_by_email(self, email: str) -> CustomerModel:
        customer = (
            self._db.query(CustomerModel).filter(CustomerModel.email == email).first()
        )
        return customer

    def login(self, login_request: LoginRequest) -> str:
        user = self.get_user_by_email(login_request.username)
        if not user and not verify_password(login_request.password, user.password):
            raise AuthException(detail={"detail": "Wrong username or password."})

        claims = Claims(
            sub=str(user.id),
            email=user.email,
            role=user.user_type,
            permissions=ROLE_PERMISSIONS[user.user_type],
        )
        return create_access_token(claims.model_dump())
