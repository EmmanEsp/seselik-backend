from fastapi import APIRouter, status, Depends

from app.entities.responses.api_response import APIResponse
from app.entities.enums import api_status
from app.customer.use_cases.customer_use_cases import GetCustomerUseCase
from app.customer.api.v1 import customer_documentation
from app.customer.entities.responses.customer_response import CustomerResponse
from app.customer.entities.requests.customer_request import CustomerRequest

customer_v1_router = APIRouter()


@customer_v1_router.get(
    "",
    response_model=APIResponse[list[CustomerResponse]],
    status_code=status.HTTP_200_OK
)
def get_all_customers(use_case: GetCustomerUseCase = Depends(GetCustomerUseCase)):
    """Get all the customer
    """
    response = use_case.get_all_customers()
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_200_OK,
        data=response)


@customer_v1_router.post(
    "",
    response_model=APIResponse[None],
    responses=customer_documentation.create_customer_responses,
    status_code=status.HTTP_201_CREATED
)
def create_customer(customer: CustomerRequest, use_case: GetCustomerUseCase = Depends(GetCustomerUseCase)):
    """Create a customer
    """
    use_case.create_customer(customer)
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_201_CREATED,
        data=None)
