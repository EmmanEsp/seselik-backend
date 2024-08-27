from fastapi import Depends
from sqlalchemy.orm import Session

from app.infraestructure.database import get_db
from app.customer.entities.models.card_payment_model import CardPaymentModel

class CardPaymentService:
    
    def __init__(self, __db: Session = Depends(get_db)) -> None:
        self.__db = __db
    
    def get_all_card_payment_by_customer_id(self, customer_id: int) -> list[CardPaymentModel]:
        return self.__db.query(CardPaymentModel).filter(CardPaymentModel.customer_id == customer_id).all()

    def create_card_payment(self, card_payment: CardPaymentModel):
        self.__db.add(card_payment)
        self.__db.commit()
