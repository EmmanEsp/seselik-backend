from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError

from app.auth.services.auth_service import AuthService
from app.security.jwt import decode_access_token
from app.security.roles_config import ROLE_PERMISSIONS

auth_scheme = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
    auth_service: AuthService = Depends(),
) -> dict:
    try:
        payload = decode_access_token(credentials.credentials.split(" ")[1])
        user_id = payload.get("sub")
        email = payload.get("email")
        role = payload.get("role")
        permissions: tuple[str] = payload.get("permissions")
        if email is None and role is None and permissions is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {
        "user_id": user_id,
        "email": email,
        "role": role,
        "permissions": permissions,
    }


def get_current_user_permission(required_permission: str):
    def check_permissions(current_user: dict = Depends(get_current_user)):
        if required_permission not in current_user["permissions"]:
            raise HTTPException(
                status_code=403,
                detail="Insufficient permissions",
            )
        return current_user

    return check_permissions
