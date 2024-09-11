from sqlalchemy import Column, Integer, String

from app.infraestructure.database import Base


class ProductStatusModel(Base):
    __tablename__ = "product_status"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
