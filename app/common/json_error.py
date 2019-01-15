# -*- coding: utf-8 -*-

class JsonError(Exception):
    def __init__(self, error, description, status_code=401, headers=None):
        Exception.__init__(self)
        self.error = error
        self.description = description
        self.status_code = status_code
        self.headers = headers

    def __repr__(self):
        return 'Error: %s' % self.error

    def __str__(self):
        return '%s. %s' % (self.error, self.description)

    def to_dict(self):
        rv = dict(())
        rv['status_code'] = self.status_code
        rv['error'] = self.error + '. ' + self.description
        rv['data'] = ''
        return rv
