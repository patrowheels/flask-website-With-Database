# here we are importing the needed blueprint method and render template method from flask
from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for
# lets us access the user model
from .models import User
# lets us store a password as a more secured data
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# this is how you define a blueprint and you chooses to call it views.
auth = Blueprint('auth', __name__)

# methods allow this route to have get and post requests


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category="error")
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout',)
# this decorator doesnt allow you to access the route unless your logged in
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


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

        user = User.query.filter_by(email=email).first()

        if user:
            flash('email already exists.', category="error")
        elif len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character.", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters", category="error")
        else:
            # this creating a new user from the User class we created in our models.py
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created!", category="Success")
            login_user(user, remember=True)

            return redirect(url_for('home.hmtl'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/bonus', methods=["GET", "POST"])
def bonus():
    # return "<p>Sign Up</p>"
    return render_template("bonus.html", user=current_user)
