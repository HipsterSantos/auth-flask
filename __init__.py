# app/__init__.py

from flask import Flask

from app.extension import db, jwt
from app.auth.views import auth_bp
def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)

    return app
