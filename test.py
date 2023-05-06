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


def test_predict_datapoint_with_values(client):
    data = {
        'Headers': {
            'assists': 2,
            'boosts': 4,
            'headshotKills': 1,
            'kills': 5,
            'longestKill': 45,
            'matchDuration': 1500,
            'revives': 1,
            'teamKills': 0,
            'vehicleDestroys': 0,
            'walkDistance': 2000,
            'weaponsAcquired': 7,
            'matchType': 'duo-fpp'
        }
    }
    response = client.post('/predictdata', json=data)
    assert response.status_code == 200
    assert b'The prediction is' in response.data