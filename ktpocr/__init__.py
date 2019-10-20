import os
from flask import Flask
from api.routes import api_routes

def init_blueprints(app):
    try:
        app.register_blueprint(api_routes)
        print('Registration Initialized')
    except Exception as e:
        print(e)
        print('Registration is NOT Initialized')
        raise

def init_config(app):
    os.environ.setdefault('KTPOCR_ENV', 'ktpocr.config.DevelopmentConfig')
    try:
        app.config.from_object(os.environ['KTPOCR_ENV'])
        print('Config Initialized')
    except Exception as e:
        print(e)
        print('Config NOT initialized')
        raise

def init_app():
    try:
        app = Flask(__name__)
        init_blueprints(app)
        init_config(app)
        print('App Initialized')
        return app
    except Exception as e:
        print(e)
        print('App is NOT Initialized')
        raise
