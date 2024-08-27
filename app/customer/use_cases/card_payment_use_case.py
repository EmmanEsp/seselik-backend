from fastapi import Depends

from app.customer.services.card_payment_service import CardPaymentService
from app.customer.entities.responses.card_payment_response import CardPaymentResponse
from app.customer.entities.requests.card_payment_request import CardPaymentRequest
from app.customer.entities.models.card_payment_model import CardPaymentModel

class CardPaymentUseCase:
    
    def __init__(self, __service: CardPaymentService = Depends()) -> None:
        self.__service = __service
    
    def get_all_card_payment_by_customer_id(self, customer_id: int) -> list[CardPaymentResponse]:
        cards: list[CardPaymentModel] = self.__service.get_all_card_payment_by_customer_id(customer_id)
        card_responses = [
            CardPaymentResponse(
                id=card.id,
                nameOnCard=card.name_on_card,
                cardNumber=card.card_number,
                monthDate=card.month_date,
                yearDate=card.year_date
            )
            for card in cards
        ]
        return card_responses
    
    def create_card_payment(self, card_payment: CardPaymentRequest):
        new_card_payment = CardPaymentModel(
            customer_id=card_payment.customerId,
            name_on_card=card_payment.nameOnCard,
            card_number=card_payment.cardNumber,
            month_date=card_payment.monthDate,
            year_date=card_payment.yearDate,
            security_number=card_payment.securityNumber
        )
        self.__service.create_card_payment(new_card_payment)
