from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from werkzeug.security import generate_password_hash
from db.config import db
from db.models import Users

admin_blueprint = Blueprint("admin", __name__)

@admin_blueprint.route("/admin")
@login_required
def list_users():
    users = Users.query.all()
    return render_template("users2.html", title="Users", user_list=users)

@admin_blueprint.route("/admin/create-user", methods=["POST"])
@login_required
def create_user():
    first_name = request.form.get("FName")
    last_name = request.form.get("LName")
    username = request.form.get("username")
    password = request.form.get("password")
    role, is_admin = "User", 1

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


    return new_user

    #return redirect(url_for("admin.list_users"))



@admin_blueprint.route('/admin/edit-user/<id>', methods=['POST'])
@login_required
def edit_user(id):
    user = Users.query.get_or_404(id)

    # get form inputs
    status = 1
    first_name = request.form.get('FName')
    last_name = request.form.get('LName')
    username = request.form.get('username')
    password = request.form.get('password', None)
    if request.form.get('isAdmin') is not None:
        is_admin = 1
    else:
        is_admin = 0

    # make changes to user record and commit to db
    user.firstName = first_name
    user.lastName = last_name
    user.username = username
    if password:
        user.password = generate_password_hash(password, method='sha256')

    user.isAdmin = is_admin

    try:
        db.session.commit()
        flash('User updated successfully!', 'success')
    except:
        flash('Could not update user. Please try again.', 'danger')

    return redirect(url_for('admin.list_users'))