from pydantic import BaseModel

class ProductStatusRequest(BaseModel):
    
    name: str
    description: str
