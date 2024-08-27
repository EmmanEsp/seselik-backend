from fastapi import APIRouter, status, Depends

from app.entities.responses.api_response import APIResponse
from app.entities.enums import api_status
from app.customer.use_cases.card_payment_use_case import CardPaymentUseCase
from app.customer.entities.responses.card_payment_response import CardPaymentResponse
from app.customer.entities.requests.card_payment_request import CardPaymentRequest

card_payment_v1_router = APIRouter()


@card_payment_v1_router.get(
    "/{customer_id}",
    response_model=APIResponse[list[CardPaymentResponse]],
    status_code=status.HTTP_200_OK
)
def get_all_card_payment_by_customer_id(customer_id: int, use_case: CardPaymentUseCase = Depends()) -> APIResponse[list[CardPaymentResponse]]:
    cards = use_case.get_all_card_payment_by_customer_id(customer_id)
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_200_OK,
        data=cards)


@card_payment_v1_router.post(
    "",
    response_model=APIResponse[None],
    status_code=status.HTTP_201_CREATED
)
def create_card_payment(new_card: CardPaymentRequest, use_case: CardPaymentUseCase = Depends()):
    use_case.create_card_payment(new_card)
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_201_CREATED,
        data=None
    )
