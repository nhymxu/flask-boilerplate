# -*- coding: utf-8 -*-
"""Example models."""

from datetime import datetime

from mongoengine import DateTimeField, DynamicDocument, StringField

from app import utils


class Example(DynamicDocument):
    meta = {"collection": "example"}

    uid = StringField(primary_key=True, default=utils.get_uuid)

    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
