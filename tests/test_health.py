from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_ok():
    request = client.get("/health")
    assert request.status_code == 200
    body = request.json()
    assert isinstance(body, dict)
    assert body.get("status") == "ok"
