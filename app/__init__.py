from flask import Flask 

def create_app():
    app  = Flask(__name__)

    from app.login.views import login_blueprint
    app.register_blueprint(login_blueprint)

    from app.home.views import home_blueprint
    app.register_blueprint(home_blueprint)
    
    return app