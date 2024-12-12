import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    FLASK_APP = os.environ.get("FLASK_APP")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_SQLALCHEMY_TABLE = "sessions"
    SESSION_TYPE = "sqlalchemy"
    SESSION_PERMANENT = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
