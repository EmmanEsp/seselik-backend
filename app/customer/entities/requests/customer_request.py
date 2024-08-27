from pydantic import BaseModel


class CustomerRequest(BaseModel):
    
    firstName: str
    lastName: str
    phoneNumber: str
    email: str
