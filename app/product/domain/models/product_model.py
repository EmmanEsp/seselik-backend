from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.infraestructure.database import Base

class ProductModel(Base):
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
