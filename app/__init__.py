from flask import Flask
import secrets
from db.config import mysql


def create_app():
    app  = Flask(__name__)

    app.config["SECRET_KEY"] = secrets.token_hex(32)
    app.config["MYSQL_HOST"] = "172.17.0.1"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "root"
    app.config["MYSQL_DB"] = "MainTruckDB"
    mysql.init_app(app)

    from app.auth.views import auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.main.views import main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app