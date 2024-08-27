from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.database import Base

class CardPaymentModel(Base):
    __tablename__ = "card_payment"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    name_on_card = Column(String, nullable=False)
    card_number = Column(String, nullable=False)
    month_date = Column(Integer, nullable=False)
    year_date = Column(Integer, nullable=False)
    security_number = Column(Integer, nullable=False)
    
    customer = relationship("CustomerModel", back_populates="card_payments")
