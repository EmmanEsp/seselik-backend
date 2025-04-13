from fastapi import Depends
from fastapi.exceptions import HTTPException

from app.customer.domain.models.customer_model import CustomerModel
from app.customer.domain.requests.customer_request import CustomerRequest
from app.customer.domain.responses.customer_response import CustomerResponse
from app.customer.services.customer_service import CustomerService
from app.security.password import hash_password


class CustomerUseCase:
    def __init__(self, customer_service: CustomerService = Depends()) -> None:
        self.customer_service = customer_service

    def create_customer(self, customer: CustomerRequest):
        customer.password = hash_password(customer.password)
        new_customer = CustomerModel(**customer.model_dump(by_alias=False))
        self.customer_service.create_customer(new_customer)

    def get_customer_by_id(self, user_id: int) -> CustomerResponse:
        customer = self.customer_service.find_by_id(id=user_id)
        if customer is None:
            raise HTTPException(status_code=401, detail="Inactive or nonexistent user")
        return CustomerResponse(
            firstName=customer.first_name,
            lastName=customer.last_name,
            phoneNumber=customer.phone_number,
            email=customer.email,
        )
