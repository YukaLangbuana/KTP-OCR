class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    ENV = 'production'
    IN_PROD = True

class StagingConfig(Config):
    ENV = 'staging'
    DEBUG = True

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True