from fastapi import FastAPI

from app.healthcheck.api.healthcheck_router import healthcheck_router
from app.customer.api.customer_router import customer_router

from app.customer.entities.exceptions.customer_exception import CustomerException, customer_exception_handler
from app.entities.exceptions.service_exception import ServiceException, service_exception_handler

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
    _app.include_router(customer_router)
    
    _app.add_exception_handler(CustomerException, customer_exception_handler)
    _app.add_exception_handler(ServiceException, service_exception_handler)
    
    return _app

app = init()
