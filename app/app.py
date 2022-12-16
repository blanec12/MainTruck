from flask import Flask
from .main import main as main_blueprint
from .auth import auth as auth_blueprint

app = Flask(__name__)

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
app.run()

# def create_app():
#     app = Flask(__name__)
#     app.register_blueprint(auth_blueprint)
#     app.register_blueprint(main_blueprint)

#     app.debug = True
#     return app
    

# if __name__ == "__main__":
#     app = create_app(__name__)
#     app.run(debug=True)