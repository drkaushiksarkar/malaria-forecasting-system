from fastapi.testclient import TestClient
from src.service.main import app

def test_root():
    c = TestClient(app)
    r = c.get("/")
    assert r.status_code == 200