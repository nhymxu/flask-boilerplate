import base64
import io

from a2wsgi import WSGIMiddleware
from dotenv import load_dotenv
from flask import request, send_file

from logics.auth_middleware import require_authentication
from logics.webserver import create_app

load_dotenv()
app = create_app()

asgi_app = WSGIMiddleware(app)


@app.before_request
def method_override():
    if request.method == 'POST' and '_method' in request.form:
        method = request.form['_method'].upper()
        if method in ['PUT', 'DELETE', 'PATCH']:
            request.environ['REQUEST_METHOD'] = method


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
