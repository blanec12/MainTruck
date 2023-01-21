from flask import Blueprint, request, render_template, redirect, flash, url_for
from db.config import db
from db.models import Users

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/login")
def login():
    return render_template("login.html")

@auth_blueprint.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")

    user = Users.query.filter_by(username=username).first()

    if user: 
        return redirect(url_for("main.index"))
    else:
        flash("Invalid credentials. Please try again.")
        return redirect(url_for("auth.login"))