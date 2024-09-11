from fastapi import Depends
from sqlalchemy.orm import Session

from app.infraestructure.database import get_db
from app.customer.domain.models.ship_address_model import ShipAddressModel


class ShipAddressService:
    
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self._db = db
    
    def get_all_ship_address_by_customer_id(self, customer_id: int) -> list[ShipAddressModel]:
        return self._db.query(ShipAddressModel).filter(ShipAddressModel.customer_id == customer_id).all()
    
    def create_ship_address(self, ship_address: ShipAddressModel) -> None:
        self._db.add(ship_address)
        self._db.commit()
