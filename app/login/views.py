from flask import Blueprint, request, render_template
from db.config import mysql

login_blueprint = Blueprint("login", __name__)

@login_blueprint.route("/login")
def login():
    return render_template("login.html")

@login_blueprint.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Users WHERE Username = %s AND Password = %s", (username, password))
    user_found = cursor.fetchone()

    if user_found: 
        render_template("home.html")
    else:
        return "<h1>ERROR: User/Password combo not found....</h1>"