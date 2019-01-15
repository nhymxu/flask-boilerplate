# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app/__init__.py."""
import os

from flask import Config
from flask_caching import Cache

config = Config(root_path='')
config.from_object(os.getenv('FLASK_CONFIG') or 'config')

cache = Cache(config=config.get('CACHE'))

if config.get('SENTRY_ENABLED', False) and config.get('SENTRY_DSL', '') != '':
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration

    sentry_sdk.init(
        dsn=config.get('SENTRY_DSL', ''),
        integrations=[FlaskIntegration()]
    )
