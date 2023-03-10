from flask import Blueprint, render_template
from flask_login import login_required

main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/")
@login_required
def index():
    return render_template("index.html")


@main_blueprint.route("/tickets")
@login_required
def tickets():
    return render_template("tickets.html")