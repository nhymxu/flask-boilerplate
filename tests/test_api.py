from web import app as flask_app
# from web import asgi_app

API_TOKEN = 'TEST_TOKEN'
flask_app.config.update({
    "SERVER_AUTH_KEY": API_TOKEN,
})


def test_index_route():
    response = flask_app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello world'


def test_protected_route(monkeypatch):
    headers = {'X-Api-Key': API_TOKEN}
    response = flask_app.test_client().get('/protected', headers=headers)

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'protected'


def test_protected_route_unauthenticated(monkeypatch):
    response = flask_app.test_client().get('/protected')

    assert response.status_code == 401
