# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['pre']
install_requires = \
['readchar>=2.0,<3.0']

setup_kwargs = {
    'name': 'pre',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
