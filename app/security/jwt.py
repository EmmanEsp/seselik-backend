from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

from app.security.security_settings import get_security_setting

ALGORITHM = "HS256"

security_settings = get_security_setting()


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(
        minutes=security_settings.access_token_expire_minutes
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, security_settings.secret_key, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict:
    try:
        return jwt.decode(token, security_settings.secret_key, algorithms=[ALGORITHM])
    except JWTError as e:
        print(e)
        return None
