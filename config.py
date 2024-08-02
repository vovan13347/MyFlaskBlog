import os

#SECRET_KEY = 'key'

class Config:
    SECRET_KEY = 'key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db') 