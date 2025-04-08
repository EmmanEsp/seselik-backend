import pytest

from app.customer.domain.exceptions.customer_exception import CustomerException


class TestCustomerException:
    def test_raise_customer_exception(self):
        with pytest.raises(CustomerException):
            raise CustomerException(detail="Test Customer Exception")
