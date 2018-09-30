from app.config import ProductionConfig
from flask import Flask
from flask_login import LoginManager
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler

login_manager = LoginManager()

def register_extensions(app):
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ('base', 'forms', 'ui', 'home', 'tables', 'data', 'additional', 'base'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_logs(app):
    basicConfig(filename='error.log', level=DEBUG)
    logger = getLogger()
    logger.addHandler(StreamHandler())


def create_app(selenium=False):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(ProductionConfig)
    if selenium:
        app.config['LOGIN_DISABLED'] = True
    register_extensions(app)
    register_blueprints(app)
    configure_logs(app)
    return app
