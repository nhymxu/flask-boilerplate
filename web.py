import base64
import io
import os

from asgiref.wsgi import WsgiToAsgi
from dotenv import load_dotenv
from flask import Flask, send_file

from logics.auth_middleware import require_authentication
from logics.error_handler import ErrorHandler


load_dotenv()
app = Flask(__name__)
app.config['SERVER_AUTH_KEY'] = os.getenv('SERVER_AUTH_KEY')
ErrorHandler(app)

asgi_app = WsgiToAsgi(app)


@app.get('/favicon.ico')
def get_favicon():
    # 1x1 transparent gif
    b64_img = "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
    b = base64.b64decode(b64_img.encode('utf-8'))
    buf = io.BytesIO(b)
    buf.seek(0)

    return send_file(buf, mimetype="image/gif")


@app.get('/')
async def hello_handler():
    return 'Hello world'


@app.get('/protected')
@require_authentication
def protected():
    return 'protected'


if __name__ == '__main__':
    app.run(debug=True)
