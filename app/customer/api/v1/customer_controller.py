from fastapi import APIRouter, status, Depends

from app.entities.responses.api_response import APIResponse
from app.entities.enums import api_status
from app.customer.entities.responses.customer_response import CustomerResponse
from app.customer.use_cases.customer_use_cases import GetCustomerUseCase

customer_v1_router = APIRouter()


@customer_v1_router.get(
    "",
    response_model=APIResponse[list[CustomerResponse]],
    status_code=status.HTTP_200_OK
)
def get_customers(use_case: GetCustomerUseCase = Depends(GetCustomerUseCase)):
    """Get all the customer
    """
    response = use_case.get_all_customers()
    return APIResponse(
        status=api_status.SUCCESS,
        status_code=status.HTTP_200_OK,
        data=response)
