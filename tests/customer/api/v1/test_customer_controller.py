from unittest.mock import MagicMock

import pytest
from faker import Faker
from fastapi.testclient import TestClient

from app.customer.domain.exceptions.customer_exception import CustomerException
from app.customer.services.customer_service import CustomerService
from app.main import app
from tests.customer.mocks.create_customer_request_mock import (
    CREATE_CUSTOMER_REQUEST_DATA,
)

fake = Faker()


class TestCustomerEndpoints:
    def test_create_customer_endpoint_status_200(self, client: TestClient):
        mock_service = MagicMock(spec=CustomerService)
        mock_service.create_customer.return_value = None

        def override_customer_service():
            return mock_service

        app.dependency_overrides[CustomerService] = override_customer_service

        response = client.post(
            "/v1/customer/signup",
            json=CREATE_CUSTOMER_REQUEST_DATA,
        )
        assert response.status_code == 201
        content = response.json()
        assert content["service_status"] == "success"

    def test_create_customer_endpoint_status_400(self, client: TestClient):
        mock_service = MagicMock(spec=CustomerService)
        mock_service.create_customer.side_effect = CustomerException(
            detail={"email": "Email already in use."}
        )

        def override_customer_service():
            return mock_service

        app.dependency_overrides[CustomerService] = override_customer_service

        response = client.post(
            "/v1/customer/signup",
            json=CREATE_CUSTOMER_REQUEST_DATA,
        )
        assert response.status_code == 400
        content = response.json()
        assert content["service_status"] == "fail"
