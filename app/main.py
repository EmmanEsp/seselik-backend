from fastapi import FastAPI

from app.healthcheck.api.healthcheck_router import healthcheck_router


def init():
    """Initialize the app
    - Configure FastAPI app
    - Configure app routes
    """
    _app = FastAPI(
        title="Seselik Services",
        description="Set of ecommerce services",
        version="0.1.0"
    )
    
    _app.include_router(healthcheck_router)
    
    return _app

app = init()
