from fastapi import Depends
from sqlalchemy.orm import Session

from app.infraestructure.database import get_db
from app.customer.entities.models.customer_model import CustomerModel

class CustomerService:
    
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self._db = db
    
    def get_all_customers(self) -> list[CustomerModel]:
        return self._db.query(CustomerModel).all()
