# -*- coding: utf-8 -*-
'''
Auto import all Class in app.models folder
class name must be same as filename

https://stackoverflow.com/a/44492879
https://www.bnmetrics.com/blog/dynamic-import-in-python3

import importlib
import inspect
import os
import pkgutil

pkg_dir = os.path.dirname(__file__)

for (module_loader, name, ispkg) in pkgutil.iter_modules([pkg_dir]):
    try:
        module = importlib.import_module('.' + name, __package__)
        locals().update({k: v for (k, v) in module.__dict__.items() if k == name and inspect.isclass(v)})
    except ImportError as err:
        print('Error:', err)
'''

# Old manual import

from .Example import Example
