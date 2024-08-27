from pydantic import BaseModel, ConfigDict


class CustomerResponse(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    
    model_config = ConfigDict(from_attributes=True)
