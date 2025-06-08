from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_flight_info_mock():
    response = client.get("/api/flight-info?airline=6E&number=502&date=2025-06-10")
    assert response.status_code == 200
    data = response.json()
    assert "airline" in data
    assert data["airline"] == "6E"
