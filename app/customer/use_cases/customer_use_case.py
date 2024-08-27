from fastapi import Depends

from app.customer.services.customer_service import CustomerService
from app.customer.entities.requests.customer_request import CustomerRequest
from app.customer.entities.models.customer_model import CustomerModel

class CustomerUseCase:
    
    def __init__(self, customer_service: CustomerService = Depends()) -> None:
        self.customer_service = customer_service

    def create_customer(self, customer: CustomerRequest):
        new_customer = CustomerModel(
            first_name=customer.firstName,
            last_name=customer.lastName,
            phone_number=customer.phoneNumber,
            email=customer.email,
            password=customer.password
        )
        self.customer_service.create_customer(new_customer)
