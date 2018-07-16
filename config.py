class Config(object):
    """Common configurations
    """


class DevelopmentConfig(Config):
    """
    Development Configurations
    """   
    
    
    DEBUG = True
class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    
class TestingConfig(Config):
    TESTING = True

config_env = {
    'development' : DevelopmentConfig,
    'production' : ProductionConfig,
    'testing' : TestingConfig,
    'default' : DevelopmentConfig
}