from pydantic import BaseModel


class CustomerResponse(BaseModel):
    name: str
    last_name: str
    phone_number: str
    email_address: str
