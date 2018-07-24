import os


class Config(object):
    """Parent Configurations"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    """Development Configuration"""
    DEBUG = True


class TestingConfig(Config):
    """Testing Configurations"""
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

config_app = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
