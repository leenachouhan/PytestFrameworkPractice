import requests
import pytest
import configparser

config = configparser.ConfigParser()
config.read('properties.ini')

@pytest.fixture
def login(scope='session'):
    data = {'username':'admin','password':'password123'}
    header = {'Content-Type': 'application/json'}
    response = requests.post(config['api']['base_url2']+config['endpoint']['login'],headers=header,json=data)
    token = response.json()['token']
    return token
    