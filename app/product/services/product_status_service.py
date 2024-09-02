from fastapi import Depends
from sqlalchemy.orm import Session

from app.infraestructure.database import get_db
from app.product.entities.models.product_status_model import ProductStatusModel


class ProductStatusService:
    
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.__db = db
        
    def get_all_product_status(self) -> list[ProductStatusModel]:
        return self.__db.query(ProductStatusModel).all()
    
    def create_product_status(self, product_status: ProductStatusModel):
        self.__db.add(product_status)
        self.__db.commit()
