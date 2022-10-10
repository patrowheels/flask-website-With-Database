from flask import Blueprint, render_template

# this is how you define a blueprint and you choose to call it views.
views = Blueprint('views', __name__)

# this is a root and in this case it needs the function right after it


@views.route('/')
def home():
    # return "<h1>Home</h1>""<h1>Welcome</h1>"
    return render_template("home.html")
