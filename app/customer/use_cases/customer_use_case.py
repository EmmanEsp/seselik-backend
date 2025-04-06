from fastapi import Depends

from app.customer.services.customer_service import CustomerService
from app.customer.domain.requests.customer_request import CustomerRequest
from app.customer.domain.models.customer_model import CustomerModel
from app.infraestructure.security import hash_password


class CustomerUseCase:
    
    def __init__(self, customer_service: CustomerService = Depends()) -> None:
        self.customer_service = customer_service

    def create_customer(self, customer: CustomerRequest):
        customer.password = hash_password(customer.password)
        new_customer = CustomerModel(**customer.model_dump(by_alias=False))
        self.customer_service.create_customer(new_customer)
