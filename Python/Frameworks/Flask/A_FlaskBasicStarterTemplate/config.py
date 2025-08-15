import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DATABASE_URI = "mysql://user@localhost/foo"


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = "sqlite:///development.db"


class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = "sqlite:///testing.db"
