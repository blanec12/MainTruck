from flask import Blueprint, request, render_template, redirect, flash, url_for
from db.config import mysql

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/login")
def login():
    return render_template("login.html")

@auth_blueprint.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Users WHERE Username = %s AND Password = %s", (username, password))
    user_found = cursor.fetchone()

    if user_found: 
        return redirect(url_for("main.index"))
    else:
        flash("Invalid credentials. Please try again.")
        return redirect(url_for("auth.login"))