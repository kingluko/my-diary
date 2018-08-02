import os
"""This file creates the different configurations under which
    the app can run
"""


class Config(object):
    """Parent Configurations"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    """Development Configuration"""
    DEBUG = True
    APP_SETTINGS = "development"


class TestingConfig(Config):
    """Testing Configurations"""
    TESTING = True
    DEBUG = True
    APP_SETTINGS = "testing"
    DATABASE_NAME = os.getenv("DATABASE_TESTS")


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

config_app = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
