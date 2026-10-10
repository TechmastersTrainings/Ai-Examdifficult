"""Pytest configuration and shared test fixtures."""

import pytest
from fastapi.testclient import TestClient
from backend.app.main import app


@pytest.fixture(scope="session")
def client() -> TestClient:
    """Fixture providing a reusable TestClient for API integration testing."""
    with TestClient(app) as test_client:
        yield test_client
