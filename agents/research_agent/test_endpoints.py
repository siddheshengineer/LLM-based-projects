from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "Research Assistant" in response.text