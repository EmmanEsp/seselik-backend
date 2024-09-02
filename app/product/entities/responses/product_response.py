from pydantic import BaseModel


class ProductResponse(BaseModel):
    
    status: str
    name: str
    description: str
    price: float
