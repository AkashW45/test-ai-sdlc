import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint_status_code():
    response = client.get("/health")
    assert response.status_code == 200

def test_health_endpoint_response_body():
    response = client.get("/health")
    assert response.json() == {"status": "ok"}

def test_status_endpoint_returns_metadata():
    response = client.get("/status")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data.get("service") == "my_service"
    assert json_data.get("version") == "1.0.0"
