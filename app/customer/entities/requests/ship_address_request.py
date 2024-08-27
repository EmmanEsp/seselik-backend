from typing import Optional
from pydantic import BaseModel


class ShipAddressRequest(BaseModel):

    customerId: int
    state: str
    city: str
    description: str
    detail: str
    postalCode: str
    exteriorNumber: str
    interiorNumber: Optional[str] = None
