from unittest.mock import MagicMock

import pytest

from app.customer.domain.exceptions.customer_exception import CustomerException
from app.customer.domain.models.customer_model import CustomerModel
from app.customer.services.customer_service import CustomerService
from tests.customer.mocks.customer_model_mock import CUSTOMER_MODEL_DATA


class TestCustomerService:
    db = MagicMock()

    def find_user_by_email(self, fake_customer: CustomerModel):
        self.db.query().filter().first.return_value = fake_customer

    def test_is_email_in_use_when_email_exists(self):
        fake_customer = CustomerModel(**CUSTOMER_MODEL_DATA)
        self.find_user_by_email(fake_customer=fake_customer)
        customer_service = CustomerService(db=self.db)

        assert customer_service.is_email_in_use(fake_customer.email) is True

    def test_create_customer_success(self):
        customer_service = CustomerService(db=self.db)
        fake_customer = CustomerModel(**CUSTOMER_MODEL_DATA)
        self.db.query().filter().first.return_value = None
        customer_service.create_customer(fake_customer)

    def test_create_customer_when_email_is_in_use(self):
        customer_service = CustomerService(db=self.db)
        fake_customer = CustomerModel(**CUSTOMER_MODEL_DATA)
        self.db.query().filter().first.return_value = True

        with pytest.raises(CustomerException):
            customer_service.create_customer(fake_customer)
