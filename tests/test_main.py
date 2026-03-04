import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint_returns_200():
    response = client.get("/health")
    assert response.status_code == 200

def test_health_endpoint_status_ok():
    response = client.get("/health")
    json_body = response.json()
    assert "status" in json_body
    assert json_body["status"] == "ok"
