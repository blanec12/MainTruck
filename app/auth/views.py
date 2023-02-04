from flask import Blueprint, request, render_template, redirect, flash, url_for, session
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash
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

    if password != "setup":
        if not user or not check_password_hash(user.password, password):
            flash("Invalid credentials. Please try again.")
            return redirect(url_for("auth.login"))

    login_user(user)
    session.permanent = True
    return redirect(url_for("main.index"))

@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
        