#  we have to import flask
from flask import Flask

# whenerver you put __init__.py  inside of a folder that folder becomes a pyhthon package file it becomes a package

# this is a function that we use to create a new flask app with a name and blueprint


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "jwhebffbkefb"

    from .views import views
    from .auth import auth
    # this means the views has no prefix
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
