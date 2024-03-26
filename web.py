from asgiref.wsgi import WsgiToAsgi
from dotenv import load_dotenv
from flask import Flask

from logics.auth_middleware import require_authentication
from logics.error_handler import ErrorHandler


load_dotenv()
app = Flask(__name__)
ErrorHandler(app)

asgi_app = WsgiToAsgi(app)


@app.get('/')
def hello_handler():
    return 'Hello world'


@app.get('/protected')
@require_authentication
async def protected():
    return 'protected'


if __name__ == '__main__':
    app.run(debug=True)
