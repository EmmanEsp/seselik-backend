from fastapi import Depends

from app.product.services.product_status_service import ProductStatusService
from app.product.entities.requests.product_status_request import ProductStatusRequest
from app.product.entities.responses.product_status_response import ProductStatusResponse


class ProductStatusUseCase:
    
    def __init__(self, service: ProductStatusService = Depends()) -> None:
        self.__service = service
    
    def get_all_product_status(self) -> list[ProductStatusResponse]:
        all_status = self.__service.get_all_product_status()
        status_response = [
            ProductStatusResponse(
                name=status.name,
                description=status.description
            )
            for status in all_status
        ]
        return status_response
    
    def create_product_status(self, product_status: ProductStatusRequest):
        self.__service.create_product_status(product_status)
