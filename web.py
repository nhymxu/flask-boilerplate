import os

from asgiref.wsgi import WsgiToAsgi
from dotenv import load_dotenv
from flask import Flask

from logics.auth_middleware import require_authentication
from logics.error_handler import ErrorHandler


load_dotenv()
app = Flask(__name__)
app.config['SERVER_AUTH_KEY'] = os.getenv('SERVER_AUTH_KEY')
ErrorHandler(app)

asgi_app = WsgiToAsgi(app)


@app.get('/')
async def hello_handler():
    return 'Hello world'


@app.get('/protected')
@require_authentication
def protected():
    return 'protected'


if __name__ == '__main__':
    app.run(debug=True)
