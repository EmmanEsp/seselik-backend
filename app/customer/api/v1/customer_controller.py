from fastapi import APIRouter, status, Depends

from app.entities.responses.api_response import APIResponse
from app.entities.enums import api_status
from app.customer.use_cases.customer_use_case import CustomerUseCase
from app.customer.api.v1 import customer_documentation
from app.customer.entities.requests.customer_request import CustomerRequest

customer_v1_router = APIRouter()


@customer_v1_router.post(
    "",
    response_model=APIResponse[None],
    responses=customer_documentation.create_customer_responses,
    status_code=status.HTTP_201_CREATED
)
def create_customer(customer: CustomerRequest, use_case: CustomerUseCase = Depends()):
    """Create a customer
    """
    use_case.create_customer(customer)
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_201_CREATED,
        data=None)
