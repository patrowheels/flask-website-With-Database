from flask import Blueprint, render_template
from flask_login import login_required, current_user

# this is how you define a blueprint and you choose to call it views.
views = Blueprint('views', __name__)

# this is a root and in this case it needs the function right after it


@views.route('/')
@login_required
def home():
    # return "<h1>Home</h1>""<h1>Welcome</h1>"
    return render_template("home.html", user=current_user)
