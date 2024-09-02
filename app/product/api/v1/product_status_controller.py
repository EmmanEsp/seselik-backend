from fastapi import APIRouter, status, Depends

from app.entities.responses.api_response import APIResponse
from app.entities.enums import api_status

from app.product.use_cases.product_status_use_case import ProductStatusUseCase
from app.product.entities.requests.product_status_request import ProductStatusRequest
from app.product.entities.responses.product_status_response import ProductStatusResponse

product_status_v1_router = APIRouter()


@product_status_v1_router.get(
    "",
    response_model=APIResponse[list[ProductStatusResponse]],
    status_code=status.HTTP_200_OK
)
def get_all_product_status(use_case: ProductStatusUseCase = Depends()) -> APIResponse[list[ProductStatusResponse]]:
    response = use_case.get_all_product_status()
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_200_OK,
        data=response
    )


@product_status_v1_router.post(
    "",
    response_model=APIResponse[None],
    status_code=status.HTTP_200_OK
)
def create_product_status(product_status: ProductStatusRequest, use_case: ProductStatusUseCase = Depends()) -> APIResponse[None]:
    use_case.create_product_status(product_status)
    return APIResponse(
        service_status=api_status.SUCCESS,
        status_code=status.HTTP_201_CREATED,
        data=None
    )
