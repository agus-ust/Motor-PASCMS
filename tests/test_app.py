from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200 and r.json()["status"] == "ok"


def test_home_shows_prototype_footer():
    r = client.get("/")
    assert r.status_code == 200 and "PROTOTYPE" in r.text
