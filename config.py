import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "?\xbd|\x0c\xd5\xe9|!\x01h\xc0\x13\x85\x89\xc5n\x1e\xd4\x94+\x86Y\x01n"
    SQLALCHEMY_DATABASE_URI = os.environ['POSTGRES_DB_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
