from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Create a test client for API requests."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities after each test for isolation."""
    original_state = deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_state)
