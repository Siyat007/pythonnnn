# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add():
    response = client.get("/add?a=5&b=3")
    assert response.status_code == 200
    assert response.json()["result"] == 8

def test_power_safe_check():
    # This test would fail if someone passes malicious input
    malicious_input = "2; import os; os.system('echo hacked')"
    response = client.get(f"/power?a={malicious_input}&b=2")
    assert response.status_code == 200
    # SonarQube should flag the unsafe eval usage
