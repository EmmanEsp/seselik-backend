from fastapi import Depends

from app.customer.services.ship_address_service import ShipAddressService
from app.customer.domain.responses.ship_address_response import ShipAddressResponse
from app.customer.domain.requests.ship_address_request import ShipAddressRequest
from app.customer.domain.models.ship_address_model import ShipAddressModel


class ShipAddressUseCase:
    
    def __init__(self, ship_address_service: ShipAddressService = Depends()) -> None:
        self.ship_address_service = ship_address_service
    
    def get_all_ship_address_by_customer_id(self, customer_id: int) -> list[ShipAddressResponse]:
        ship_addresses = self.ship_address_service.get_all_ship_address_by_customer_id(customer_id)
        
        ship_address_responses = [
            ShipAddressResponse(
                id=ship_address.id,
                state=ship_address.state,
                city=ship_address.city,
                description=ship_address.description,
                detail=ship_address.detail,
                postalCode=ship_address.postal_code,
                exteriorNumber=ship_address.exterior_number,
                interiorNumber=ship_address.interior_number
            )
            for ship_address in ship_addresses
        ]
        
        return ship_address_responses
    
    def create_ship_address(self, ship_address: ShipAddressRequest) -> None:
        new_ship_address = ShipAddressModel(
            customer_id=ship_address.customerId,
            state=ship_address.state,
            city=ship_address.city,
            description=ship_address.description,
            detail=ship_address.detail,
            postal_code=ship_address.postalCode,
            exterior_number=ship_address.exteriorNumber,
            interior_number=ship_address.interiorNumber
        )
        self.ship_address_service.create_ship_address(new_ship_address)
