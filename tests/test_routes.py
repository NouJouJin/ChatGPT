import pytest
from app import create_app, db
from app.models import Product

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        db.session.add_all([
            Product(name='Apples', quantity=20),
            Product(name='Oranges', quantity=15),
            Product(name='Potatoes', quantity=30),
        ])
        db.session.commit()
    with app.test_client() as client:
        yield client

def test_product_listing(client):
    response = client.get('/')
    assert response.status_code == 200
    # Ensure at least one product name appears in the response
    assert b'Apples' in response.data
