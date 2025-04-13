from pydantic import BaseModel


class Claims(BaseModel):
    sub: str
    email: str
    role: str
    permissions: tuple
    exp: int = 60
