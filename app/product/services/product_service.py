from fastapi import Depends
from sqlalchemy.orm import Session

from app.infraestructure.database import get_db
from app.product.entities.models.product_model import ProductModel
from app.product.entities.responses.product_response import ProductResponse


class ProductService:
    
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.__db = db
        
    def get_all_products(self) -> list[ProductResponse]:
        return self.__db.query(ProductModel).all()
    
    def create_product(self, product: ProductModel):
        self.__db.add(product)
        self.__db.commit()
