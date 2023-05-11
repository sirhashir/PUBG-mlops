import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data 

def test_home(client):
    response = client.get('/predictdata')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data
    assert b'Player Stats' in response.data