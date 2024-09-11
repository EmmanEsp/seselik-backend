from pydantic import BaseModel, ConfigDict


class CustomerResponse(BaseModel):
    firstName: str
    lastName: str
    phoneNumber: str
    email: str
