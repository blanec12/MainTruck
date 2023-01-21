from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash
from db.config import db
from db.models import Users
from flask import jsonify

admin_blueprint = Blueprint("admin", __name__)

@admin_blueprint.route("/admin")
def list_users():
    users = Users.query.all()
    return render_template("users.html", title="Users", user_list=users)

@admin_blueprint.route("/admin/create-user", methods=["POST"])
def create_user():
    first_name = request.form.get("FName")
    last_name = request.form.get("LName")
    username = request.form.get("username")
    password = request.form.get("password")
    role = "User"

    if request.form.get("isAdmin") is not None:
        role = "Administrator"
        is_admin = 1

    user = Users.query.filter_by(username=username).first()

    if user: 
        flash('Username could not be created. Username already exists.', 'danger' )
        return redirect(url_for('admin.list_users'))
    

    new_user = Users(firstName=first_name, lastName=last_name, username=username, password=generate_password_hash(password, method='sha256'), isAdmin=is_admin)

    try:
        db.session.add(new_user)
        db.session.commit()
        flash('User successfully created!', 'success')
    except:
        flash('User could not be created. Please try again.', 'danger')

    return redirect(url_for("admin.list_users"))