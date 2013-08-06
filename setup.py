try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'LoFi',
    'author': 'Desmond Morris',
    'author_email': 'hi@desmondmorris.com',
    'version': '0.0.1',
    'install_requires': ['Flask', 'Flask-MongoEngine', 'nose'],
    'packages': ['lofi'],
    'scripts': [],
    'name': 'LoFi'
}

setup(**config)