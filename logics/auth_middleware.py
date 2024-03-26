import os
from functools import wraps

from flask import request

from .exceptions import APIException


class AuthMiddleware:

    @staticmethod
    def is_valid_token(token):
        secret_key = os.getenv('SERVER_AUTH_KEY')

        return token == secret_key

    def authenticate(self):
        auth_token = request.headers.get('X-Api-Key')

        if not auth_token or not self.is_valid_token(auth_token):
            raise APIException('Unauthorized', 401)


def require_authentication(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        AuthMiddleware().authenticate()
        return func(*args, **kwargs)

    return wrapper
