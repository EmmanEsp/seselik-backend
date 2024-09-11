from pydantic import BaseModel, ConfigDict

class CardPaymentRequest(BaseModel):
    
    customerId: int
    nameOnCard: str
    cardNumber: str
    monthDate: int
    yearDate: int
    securityNumber: int
    
    model_config = ConfigDict(from_attributes=True)
