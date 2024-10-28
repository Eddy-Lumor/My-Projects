import os

class Config:
    # Secret key for session management, CSRF protection, etc.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'

    # SQLAlchemy database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'

    # SQLAlchemy modification tracking setting (turn it off to save resources)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Other configurations (if needed)
    DEBUG = True 

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    WTF_CSRF_ENABLED = False