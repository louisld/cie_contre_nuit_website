import os

class BaseConfig():
    SECRET_KEY = os.getenv("SECRET_KEY")
    STATIC_DIR = "static/assets"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevelopmentConfig(BaseConfig):
    DEBUG=True
    ENV='development'
    VITE_URL_DEV = os.getenv("VITE_URL_DEV", "http://localhost:5173")

class ProductionConfig(BaseConfig):
    DEBUG=False
    ENV='production'

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}