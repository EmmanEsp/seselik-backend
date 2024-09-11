from pydantic import BaseModel

class ProductRequest(BaseModel):
    
    status: str
    name: str
    description: str
    price: float
