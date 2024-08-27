from fastapi import Depends

from app.customer.services.customer_service import CustomerService
from app.customer.entities.responses.customer_response import CustomerResponse

class GetCustomerUseCase:
    
    def __init__(self, customer_service: CustomerService = Depends(CustomerService)) -> None:
        self.customer_service = customer_service
    
    def get_all_customers(self) -> list[CustomerResponse]:
        customers = self.customer_service.get_all_customers()
        customer_responses = [CustomerResponse.model_validate(customer) for customer in customers]
        return customer_responses
