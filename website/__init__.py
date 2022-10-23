#  we have to import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#
db = SQLAlchemy()
DB_NAME = "database.db"


# whenerver you put __init__.py  inside of a folder that folder becomes a pyhthon package file it becomes a package

# this is a function that we use to create a new flask app with a name and blueprint


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "jwhebffbkefb"
    # this will store database inside the directory that the init_py file is in aka website folder
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initialize our database by giving it our flask app
    db.init_app(app)

    from .views import views
    from .auth import auth

    # this means the views has no prefix
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # .get will be looking for the int version of the primary key
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
