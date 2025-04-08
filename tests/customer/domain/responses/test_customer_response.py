import pytest
from faker import Faker

from app.customer.domain.responses.customer_response import CustomerResponse

fake = Faker()


class TestCustomerResponse:
    def test_valid_data(self):
        data = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "phoneNumber": fake.phone_number(),
            "email": fake.email(),
        }

        customer_response = CustomerResponse(**data)

        assert customer_response.first_name
        assert customer_response.email
