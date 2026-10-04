from fastapi.testclient import TestClient
from app.main import app


def test_health_is_available():
    client = TestClient(app)
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'


def test_payment_is_fail_closed_by_default():
    client = TestClient(app)
    response = client.post('/v1/checkout/quote', json={'wallet': '0x' + '1' * 40})
    assert response.status_code == 503
