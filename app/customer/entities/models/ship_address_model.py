from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.database import Base

class ShipAddressModel(Base):
    __tablename__ = "ship_address"
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    state = Column(String)
    city = Column(String)
    description = Column(String)
    detail = Column(String)
    postal_code = Column(String)
    exterior_number = Column(String)
    interior_number = Column(String)

    customer = relationship("CustomerModel", back_populates="addresses")
