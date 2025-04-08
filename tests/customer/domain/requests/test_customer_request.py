import pytest
from pydantic import ValidationError

from app.customer.domain.requests.customer_request import CustomerRequest
from tests.customer.mocks.create_customer_request_mock import (
    CREATE_CUSTOMER_REQUEST_DATA,
)


class TestCustomerRequest:
    def test_valid_data(self):
        customer = CustomerRequest(**CREATE_CUSTOMER_REQUEST_DATA)
        assert customer.first_name
        assert customer.email

    def test_invalid_password_too_short(self):
        CREATE_CUSTOMER_REQUEST_DATA["password"] = "123"
        with pytest.raises(ValidationError) as exc_info:
            CustomerRequest(**CREATE_CUSTOMER_REQUEST_DATA)
        assert "password" in str(exc_info.value)

    def test_invalid_email(self):
        CREATE_CUSTOMER_REQUEST_DATA["email"] = "email."
        with pytest.raises(ValidationError) as exc_info:
            CustomerRequest(**CREATE_CUSTOMER_REQUEST_DATA)
        assert "email" in str(exc_info.value)
