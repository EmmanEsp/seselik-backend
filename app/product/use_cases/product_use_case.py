from fastapi import Depends

from app.product.services.product_service import ProductService
from app.product.domain.responses.product_response import ProductResponse
from app.product.domain.requests.product_request import ProductRequest
from app.product.domain.models.product_model import ProductModel


class ProductUseCase:
    
    def __init__(self, service: ProductService = Depends()) -> None:
        self.__service = service
        
    def get_all_products(self) -> list[ProductResponse]:
        products = self.__service.get_all_products()
        product_response = [
            ProductResponse(
                description=product.description,
                name=product.name,
                price=product.price,
                status=product.status
            )
            for product in products
        ]
        return product_response

    def create_product(self, product: ProductRequest):
        new_product = ProductModel(
            status=product.status,
            name=product.name,
            description=product.description,
            price=product.price
        )
        self.__service.create_product(new_product)
