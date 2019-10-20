import os
from flask import Flask

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
        init_config(app)
        print('App Initialized')
        return app
    except Exception as e:
        print(e)
        print('App is NOT Initialized')
        raise
