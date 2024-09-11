from fastapi import APIRouter, status, Depends

from app.domain.responses.api_response import APIResponse
from app.domain.enums import api_status
from app.customer.domain.responses.ship_address_response import ShipAddressResponse
from app.customer.domain.requests.ship_address_request import ShipAddressRequest
from app.customer.use_cases.ship_address_use_case import ShipAddressUseCase

ship_address_v1_router = APIRouter()


@ship_address_v1_router.get(
    "/{customer_id}",
    response_model=APIResponse[list[ShipAddressResponse]],
    status_code=status.HTTP_200_OK
)
def get_all_addresses_by_customer_id(customer_id: int, use_case: ShipAddressUseCase = Depends()):
    ship_address_reponses = use_case.get_all_ship_address_by_customer_id(customer_id)
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_200_OK,
        data=ship_address_reponses
    )
    

@ship_address_v1_router.post(
    "",
    response_model=APIResponse[None],
    status_code=status.HTTP_201_CREATED
)
def create_ship_address(payload: ShipAddressRequest, use_case: ShipAddressUseCase = Depends()):
    use_case.create_ship_address(payload)
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_201_CREATED,
        data=None
    )
