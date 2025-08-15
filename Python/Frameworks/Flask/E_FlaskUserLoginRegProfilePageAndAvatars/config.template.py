import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DATABASE_URI = "mysql://user@localhost/foo"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = "sqlite:///development.db"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")


class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = "sqlite:///testing.db"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
