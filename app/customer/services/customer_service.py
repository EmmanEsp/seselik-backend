from fastapi import Depends
from sqlalchemy.orm import Session

from app.customer.domain.exceptions.customer_exception import CustomerException
from app.customer.domain.models.customer_model import CustomerModel
from app.infraestructure.database import get_db


class CustomerService:

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self._db = db

    def find_by_id(self, id: int) -> CustomerModel:
        return self._db.query(CustomerModel).filter(CustomerModel.id == id).first()

    def is_email_in_use(self, email: str) -> bool:
        customer = (
            self._db.query(CustomerModel).filter(CustomerModel.email == email).first()
        )
        return customer is not None

    def create_customer(self, customer: CustomerModel):
        if self.is_email_in_use(customer.email):
            raise CustomerException(detail={"email": "Email already in use."})
        self._db.add(customer)
        self._db.commit()
