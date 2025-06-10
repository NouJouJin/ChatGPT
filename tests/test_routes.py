import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_product_listing(client):
    response = client.get('/')
    assert response.status_code == 200
    # Ensure at least one product name appears in the response
    assert b'Apples' in response.data
