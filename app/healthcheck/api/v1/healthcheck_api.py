"""Healthcheck API
"""
from fastapi import APIRouter, status

from app.healthcheck.entities.responses.get_healthcheck_response import GetHealthcheckResponse

healthcheck_v1_router = APIRouter()


@healthcheck_v1_router.get(
    "",
    response_model=GetHealthcheckResponse,
    status_code=status.HTTP_200_OK
)
def get_healthcheck():
    """Check and return status of the service health
    """
    return GetHealthcheckResponse(status=status.HTTP_200_OK, content="OK")
