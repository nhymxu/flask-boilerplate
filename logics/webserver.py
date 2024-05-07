import os

from flask import Flask

from logics.error_handler import ErrorHandler


def create_app():
    app = Flask(__name__)
    app.config['SERVER_AUTH_KEY'] = os.getenv('SERVER_AUTH_KEY')
    ErrorHandler(app)

    return app
