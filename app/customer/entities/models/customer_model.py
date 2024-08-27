from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.infraestructure.database import Base


class CustomerModel(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, unique=True)
    
    addresses = relationship("ShipAddressModel", back_populates="customer")
    card_payments = relationship("CardPaymentModel", back_populates="customer")
