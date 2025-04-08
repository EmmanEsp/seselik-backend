import pytest
from faker import Faker

from app.customer.domain.models.customer_model import CustomerModel
from tests.customer.mocks.create_customer_request_mock import (
    CREATE_CUSTOMER_REQUEST_MOCK,
)

fake = Faker()


class TestCustomerModel:
    def test_create_customer_model(self):
        customer_model = CustomerModel(
            **CREATE_CUSTOMER_REQUEST_MOCK.model_dump(by_alias=False)
        )
        assert customer_model.first_name
        assert customer_model.email
