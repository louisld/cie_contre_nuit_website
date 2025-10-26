from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_sitemap import Sitemap


db= SQLAlchemy()
migrate = Migrate()
sitemap = Sitemap()