from fastapi import APIRouter, Depends, status

from app.customer.api.v1 import customer_documentation
from app.customer.domain.requests.customer_request import CustomerRequest
from app.customer.domain.responses.customer_response import CustomerResponse
from app.customer.use_cases.customer_use_case import CustomerUseCase
from app.domain.enums import api_status
from app.domain.responses.api_response import APIResponse
from app.security.auth_handler import get_current_user_permission

customer_v1_router = APIRouter()


@customer_v1_router.post(
    "",
    response_model=APIResponse[None],
    responses=customer_documentation.create_customer_responses,
    status_code=status.HTTP_201_CREATED,
)
def create_customer(customer: CustomerRequest, use_case: CustomerUseCase = Depends()):
    """Create a customer"""
    use_case.create_customer(customer)
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_201_CREATED,
        data=None,
    )


@customer_v1_router.post(
    "/me",
    response_model=APIResponse[CustomerResponse],
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
)
def get_me_info(
    current_user: dict = Depends(
        get_current_user_permission(required_permission="view")
    ),
    use_case: CustomerUseCase = Depends(),
):
    """Create a customer"""
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_200_OK,
        data=use_case.get_customer_by_id(user_id=current_user["user_id"]),
    )
