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


def test_predict_data_page(client):
    # Make GET request to /predictdata
    response = client.get('/predictdata')

    # Assert that response is successful and contains the correct content
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data
    assert b'Player Stats' in response.data
    assert b'Assists:' in response.data
    assert b'Boosts:' in response.data 
    assert b'Headshot Kills:' in response.data
    assert b'Kills:' in response.data
    assert b'Longest Kill:' in response.data
    assert b'Match Duration:' in response.data
    assert b'Revives:' in response.data
    assert b'Team Kills:' in response.data
    assert b'Vehicle Destroys:' in response.data
    assert b'Walk Distance:' in response.data
    assert b'Weapons Acquired:' in response.data
    assert b'Match Type:' in response.data
    assert b'Predict your pubg Score' in response.data
    assert b'The prediction is ' in response.data

def test_predict_datapoint_with_values(client):
    response = client.post('/predictdata', data={
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
    })
    assert response.status_code == 200
    assert b'The prediction is' in response.data
