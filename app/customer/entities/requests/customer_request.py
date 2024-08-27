from pydantic import BaseModel


class CustomerRequest(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
