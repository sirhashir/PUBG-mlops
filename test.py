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


def test_predict_datapoint(client):
    data = {
        "Headers": {
            "data": {
                "assists": 1,
                "boosts": 5,
                "headshotKills": 10,
                "kills": 10,
                "longestKill": 500,
                "matchDuration": 1200,
                "revives": 1,
                "teamKills": 0,
                "vehicleDestroys": 0,
                "walkDistance": 2000,
                "weaponsAcquired": 5,
                "matchType": "solo"
            }
        }
    }

    response = client.post('/predictdata', json=data)
    assert response.status_code == 200
    print(response)
    assert isinstance(response.data.decode('utf-8'), str)

def test_predict_datapoint_with_missing_data(client):
    data = {
        "Headers": {
            "data": {
                "assists": 0,
                "boosts": 0,
                "headshotKills": 0,
                "kills": 0,
                "longestKill": 0,
                "matchDuration": 0,
                "revives": 0,
                "teamKills": 0,
                "vehicleDestroys": 0,
                "walkDistance": 0,
                "weaponsAcquired": 0,
                "matchType": "squad-fpp"
            }
        }
    }
    response = client.post('/predictdata', json=data)
    assert response.status_code == 200
    assert isinstance(response.data.decode('utf-8'), str)

def test_predict_datapoint_with_invalid_matchtype(client):
    data = {
        "Headers": {
            "data": {
                "assists": 1,
                "boosts": 2,
                "headshotKills": 1,
                "kills": 12,
                "longestKill": 10.5,
                "matchDuration": 2000,
                "revives": 0,
                "teamKills": 0,
                "vehicleDestroys": 0,
                "walkDistance": 50,
                "weaponsAcquired": 3,
                "matchType": "invalid-match-type"
            }
        }
    }
    response = client.post('/predictdata', json=data)
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "The provided 'matchType' value is invalid. Allowed values are ['solo', 'solo-fpp', 'duo', 'duo-fpp', 'squad', 'squad-fpp']." 
