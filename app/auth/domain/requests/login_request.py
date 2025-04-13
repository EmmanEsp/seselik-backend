from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    username: EmailStr
    password: str = Field(..., min_length=6, max_length=24)
