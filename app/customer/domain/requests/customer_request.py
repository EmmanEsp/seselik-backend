from pydantic import BaseModel, EmailStr, Field


class CustomerRequest(BaseModel):
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    phone_number: str = Field(..., alias="phoneNumber")
    email: EmailStr = Field(...)
    password: str = Field(
        ..., description="Contraseña de usuario", min_length=8, max_length=24
    )
