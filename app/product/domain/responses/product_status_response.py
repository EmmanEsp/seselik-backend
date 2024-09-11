from pydantic import BaseModel

class ProductStatusResponse(BaseModel):
    
    name: str
    description: str
