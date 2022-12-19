from flask import Blueprint, render_template


login_blueprint = Blueprint("login", __name__)
@login_blueprint.route("/login")
def login():
    return render_template("login.html")

@login_blueprint.route("/somethingelse")
def somethingElse():
    return "<h1>Hlep</h1>"