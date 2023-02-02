from flask import Flask
from flask_login import LoginManager
from datetime import timedelta
import secrets
from db.config import db
from db.models import Users


def create_app():
    app  = Flask(__name__)

    app.config["SECRET_KEY"] = secrets.token_hex(32)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@172.17.0.1/MainTruckDB"
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=10)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    from app.auth.views import auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.main.views import main_blueprint
    app.register_blueprint(main_blueprint)

    from app.admin.views import admin_blueprint
    app.register_blueprint(admin_blueprint)
    
    return app