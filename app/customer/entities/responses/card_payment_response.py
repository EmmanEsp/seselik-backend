from pydantic import BaseModel, ConfigDict

class CardPaymentResponse(BaseModel):
    
    id: int
    nameOnCard: str
    cardNumber: str
    monthDate: int
    yearDate: int
    
    model_config = ConfigDict(from_attributes=True)
