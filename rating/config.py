import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 's5df46sf46s46dfgvfbfbfhGFGFGFB56BF'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'rating.db')
