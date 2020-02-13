from starlette.testclient import TestClient
import sys
import os.path
# FIXME: find more elegant way to use absolute import
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from main import app

client = TestClient(app)

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "<head>" in response.text
