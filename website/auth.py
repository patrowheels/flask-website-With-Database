# here we are importing the needed blueprint method and render template method from flask
from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for
# lets us access the user model
from .models import User
# lets us store a password as a more secured data
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

# this is how you define a blueprint and you chooses to call it views.
auth = Blueprint('auth', __name__)

# methods allow this route to have get and post requests


@auth.route('/login', methods=["GET", "POST"])
def login():
    # return "<p>Login</p>"
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route('/logout',)
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    # return "<p>Sign Up</p>"
    data = request.form
    print(data)

    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character.", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters", category="error")
        else:
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created!", category="Success")
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")


@auth.route('/bonus', methods=["GET", "POST"])
def bonus():
    # return "<p>Sign Up</p>"
    return render_template("bonus.html")
