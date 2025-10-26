import os

class BaseConfig():
    SECRET_KEY = os.getenv("SECRET_KEY")
    STATIC_DIR = "static/assets"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS = os.environ.get("SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS", True)
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,             
        'pool_recycle': 1800,       
        'pool_size': 10,            
        'max_overflow': 20  
    }


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