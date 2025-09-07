from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_stations_pagination():
    r = client.get("/stations?limit=2&offset=0")
    assert r.status_code == 200
    body = r.json()
    assert set(body.keys()) == {"data", "meta"}
    assert isinstance(body["data"], list)
    assert len(body["data"]) <= 2
    meta = body["meta"]
    assert {"total", "limit", "offset"} <= set(meta.keys())
    assert meta["limit"] == 2
    assert meta["offset"] == 0

def test_list_stations_item_shape():
    r = client.get("/stations?limit=1")
    assert r.status_code == 200
    item = r.json()["data"][0]
    assert {"id", "name", "latitude", "longitude", "status", "connectors"} <= set(item.keys())
    assert isinstance(item["connectors"], list)

def test_update_station_status_ok():
    payload = {"status": "AVAILABLE"}
    r = client.patch("/stations/S-002/status", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == "S-002"
    assert body["status"] == "AVAILABLE"

def test_update_station_status_invalid_value():
    payload = {"status": "NOT_A_STATUS"}
    r = client.patch("/stations/S-002/status", json=payload)
    assert r.status_code == 422

def test_update_station_status_not_found():
    payload = {"status": "AVAILABLE"}
    r = client.patch("/stations/DOES-NOT-EXIST/status", json=payload)
    assert r.status_code == 404
    body = r.json()
    assert body.get("error") == "not_found"
    assert "not found" in (body.get("detail") or "").lower()
