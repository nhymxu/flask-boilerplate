# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app/__init__.py."""
import os

from flask import Config
from flask_caching import Cache

config = Config(root_path='')
config.from_object(os.getenv('FLASK_CONFIG') or 'config')

cache = Cache(config=config.get('CACHE'))

if config.get("MONGO_URI", None):
    from mongoengine import connect

    db = connect(alias="default", host=config.get("MONGO_URI", "localhost"))

if config.get('REDIS_URL', None):
    from redis import StrictRedis

    db_redis = StrictRedis.from_url(config.get("REDIS_URL", "redis://localhost:6379/0"))

if config.get('SENTRY_ENABLED', False) and config.get('SENTRY_DSL', '') != '':
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration

    release_version = config.get('RELEASE_VERSION', None)
    if release_version:
        sentry_release = "flask-base@" + release_version
        sentry_sdk.init(
            dsn=config.get('SENTRY_DSL', ''),
            integrations=[FlaskIntegration()],
            release=sentry_release
        )
    else:
        sentry_sdk.init(
            dsn=config.get('SENTRY_DSL', ''),
            integrations=[FlaskIntegration()]
        )
