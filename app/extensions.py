from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_sitemap import Sitemap
from flask_login import LoginManager


db= SQLAlchemy()
migrate = Migrate()
sitemap = Sitemap()
login_manager = LoginManager()

login_manager.login_view = "auth.login"