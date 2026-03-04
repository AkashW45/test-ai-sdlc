import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_status_code():
    response = client.get("/health")
    assert response.status_code == 200

def test_health_response_body():
    response = client.get("/health")
    assert response.json().get("status") == "ok"

def test_status_endpoint():
    response = client.get("/status")
    assert response.status_code == 200
    json = response.json()
    assert json.get("service") == "my_service"
    assert json.get("version") == "1.0.0"
