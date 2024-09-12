import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from web import app as flask_app
# from web import asgi_app

API_TOKEN = 'TEST_TOKEN'
flask_app.config.update({"SERVER_AUTH_KEY": API_TOKEN})

@pytest.fixture
def client():
    """Set up a test client for the app with setup and teardown logic."""
    with flask_app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello world'


def test_protected_route(client, monkeypatch):
    headers = {'X-Api-Key': API_TOKEN}
    response = client.get('/protected', headers=headers)

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'protected'


def test_protected_route_unauthenticated(client, monkeypatch):
    response = client.get('/protected')

    assert response.status_code == 401
