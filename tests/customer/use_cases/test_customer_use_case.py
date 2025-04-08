from unittest.mock import MagicMock

import pytest

from app.customer.domain.exceptions.customer_exception import CustomerException
from app.customer.domain.requests.customer_request import CustomerRequest
from app.customer.use_cases.customer_use_case import CustomerUseCase
from tests.customer.mocks.create_customer_request_mock import (
    CREATE_CUSTOMER_REQUEST_MOCK,
)


class TestCustomerUseCase:

    def test_create_customer_success(self):
        customer_service = MagicMock()
        customer_use_case = CustomerUseCase(customer_service=customer_service)
        assert (
            customer_use_case.create_customer(customer=CREATE_CUSTOMER_REQUEST_MOCK)
            is None
        )

    def test_create_customer_is_email_use(self):
        customer_service = MagicMock()
        customer_service.create_customer.side_effect = CustomerException(
            detail={"email": "Email already in use."}
        )
        customer_use_case = CustomerUseCase(customer_service=customer_service)

        with pytest.raises(CustomerException):
            customer_use_case.create_customer(customer=CREATE_CUSTOMER_REQUEST_MOCK)
