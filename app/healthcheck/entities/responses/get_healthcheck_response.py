"""Get healthcheck api response schema
"""
from pydantic import BaseModel


class GetHealthcheckResponse(BaseModel):
    """Response for get healthcheck endpoint
    """
    
    status: int
    content: str
