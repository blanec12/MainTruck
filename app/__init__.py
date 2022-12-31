from flask import Flask
import secrets
from db.config import mysql


def create_app():
    app  = Flask(__name__)

    app.config['SECRET_KEY'] = secrets.token_hex(32)
    app.config['MYSQL_HOST'] = '172.17.0.1'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'MainTruckDB'
    mysql.init_app(app)

    from app.login.views import login_blueprint
    app.register_blueprint(login_blueprint)

    from app.home.views import home_blueprint
    app.register_blueprint(home_blueprint)
    
    return app