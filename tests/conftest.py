"""
Confest Testing file
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """
    Fixture client app
    """
    with TestClient(app) as client:
        yield client
