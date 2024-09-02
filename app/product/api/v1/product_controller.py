from fastapi import APIRouter, Depends, status

from app.entities.responses.api_response import APIResponse
from app.entities.enums import api_status
from app.product.entities.requests.product_request import ProductRequest
from app.product.entities.responses.product_response import ProductResponse
from app.product.use_cases.product_use_case import ProductUseCase

product_v1_router = APIRouter()


@product_v1_router.get(
    "",
    response_model=APIResponse[list[ProductResponse]],
    status_code=status.HTTP_200_OK
)
def get_all_products(use_case: ProductUseCase = Depends()) -> APIResponse[list[ProductResponse]]:
    products = use_case.get_all_products()
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_200_OK,
        data=products
    )


@product_v1_router.post(
    "",
    response_model=APIResponse[None],
    status_code=status.HTTP_201_CREATED
)
def create_product(product: ProductRequest, use_case: ProductUseCase = Depends()) -> APIResponse[None]:
    use_case.create_product(product)
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_201_CREATED,
        data=None
    )
