"""Import OS"""
import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base Config to be inherited from"""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://localhost/dke_ffball')


class ProductionConfig(Config):
    """Production Config variables go here"""
    DEBUG = False


class StagingConfig(Config):
    """Staging Config variables go here"""
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    """Development Config variables go here"""
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """Testing Config variables go here"""
    TESTING = True
