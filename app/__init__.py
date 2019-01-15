# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""

from flask import Flask, jsonify
from flask_cors import CORS

# Import module
from app import commands, extensions
from app.common.json_error import JsonError

from app.v1 import starter


def create_app():
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    """
    app = Flask(__name__)

    # app.url_map.strict_slashes = False
    # app.config.from_object('config')

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    CORS(app)
    extensions.cache.init_app(app, config={'CACHE_TYPE': 'simple'})


def register_blueprints(app):
    """Register Flask blueprints."""

    # API common

    # API v1
    app.register_blueprint(starter.routes.blueprint, url_prefix='/v1/starter')


def register_errorhandlers(app):
    def handle_json_error(error):
        response = jsonify(error.to_dict())
        # response = error.to_json()
        response.status_code = error.status_code
        return response

    app.errorhandler(JsonError)(handle_json_error)


def register_shellcontext(app):
    """Register shell context objects."""
    pass


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
