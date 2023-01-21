from flask import Flask
import secrets
from db.config import db


def create_app():
    app  = Flask(__name__)

    app.config["SECRET_KEY"] = secrets.token_hex(32)
    # app.config["MYSQL_HOST"] = "172.17.0.1"
    # app.config["MYSQL_USER"] = "root"
    # app.config["MYSQL_PASSWORD"] = "root"
    # app.config["MYSQL_DB"] = "MainTruckDB"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@172.17.0.1/MainTruckDB'
    db.init_app(app)

    from app.auth.views import auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.main.views import main_blueprint
    app.register_blueprint(main_blueprint)

    from app.admin.views import admin_blueprint
    app.register_blueprint(admin_blueprint)
    
    return app