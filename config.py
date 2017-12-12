"""Import OS"""
import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base Config to be inherited from"""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://fquaejmwwfaljp:60198a7ab16747274a3e6cd709a3741388ceb00f11df30d2f5afb4e67d904b41@ec2-107-22-165-47.compute-1.amazonaws.com:5432/d3ub9g35sd54fp')


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
