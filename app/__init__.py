import os

from dotenv import load_dotenv

from flask import Flask

from config import BaseConfig, config_by_name

from app.main import main
from app.helpers.vite import vite_asset

def create_app():
    app = Flask(__name__)
    
    load_config(app)
    define_blueprints(app)
    configure_jinja(app)

    return app

def load_config(app: Flask):
    basedir = os.path.abspath(os.path.dirname(__file__))
    dotenv_path = os.path.join(basedir, "../.env")

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        import sys
        print("The .env file is missing.")
        sys.exit(1)
    
    env = os.getenv("FLASK_ENV", 'development')
    app.config.from_object(config_by_name.get(env, 'development'))

def define_blueprints(app: Flask):
    app.register_blueprint(main)

def configure_jinja(app: Flask):
    @app.context_processor
    def inject_vite_asset():
        return dict(vite_asset=vite_asset)