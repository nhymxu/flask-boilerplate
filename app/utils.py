# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import hashlib

from simpleflake import simpleflake


def get_uuid():
    return str(simpleflake())


def md5(text):
    return hashlib.md5(str(text).encode('utf-8')).hexdigest()
