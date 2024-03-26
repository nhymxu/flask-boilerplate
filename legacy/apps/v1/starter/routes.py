# -*- coding: utf-8 -*-

from flask import Blueprint

blueprint = Blueprint('v1_starter', __name__)


@blueprint.route('/', methods=['GET'])
def get_starter():
    return 'Hello page'
