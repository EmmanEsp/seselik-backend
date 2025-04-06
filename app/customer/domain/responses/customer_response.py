from pydantic import BaseModel, Field


class CustomerResponse(BaseModel):
    first_name: str =  Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    phone_number: str = Field(alias="phoneNumber")
    email: str
