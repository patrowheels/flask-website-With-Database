# here we are importing the needed blueprint method and render template method from flask
from flask import Blueprint, render_template

# this is how you define a blueprint and you chooses to call it views.
auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    # return "<p>Login</p>"
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up')
def sign_up():
    # return "<p>Sign Up</p>"
    return render_template("sign_up.html")


@auth.route('/bonus')
def bonus():
    # return "<p>Sign Up</p>"
    return render_template("bonus.html")
