class Config(object):
    SECRET_KEY = 'key'
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class DebugConfig(Config):
    DEBUG = True
