from fastapi import APIRouter, status

from app.customer.entities.responses.customer_response import CustomerResponse
from app.entities.responses.api_response import APIResponse
from app.entities.enums import api_status

customer_v1_router = APIRouter()


@customer_v1_router.get(
    "",
    response_model=APIResponse[list[CustomerResponse]],
    status_code=status.HTTP_200_OK
)
def get_customers():
    """Get all the customer
    """
    return APIResponse(
        status=api_status.SUCCESS,
        status_code=status.HTTP_200_OK,
        data=[CustomerResponse(
            name="Jose", 
            last_name="Espinoza", 
            phone_number="6677282723",
            email_address="jose.espinoza@gmail.com")])
