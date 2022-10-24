# this is where we create our 2 database models
# one database for our notes and another database for our users


from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# this inherits from db.Model this is a blueprint for a Note object that will be stored in database
class Note(db.Model):

    id = db.Column(db.Integer, primary_key=True)
#
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # we use foreign key when we have on user object that can save many note objects
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
# this above foreignKey here is only when you have a one to many relatiosnhip

# db is the sql object that we created
# whenever you want to make a new database model(store a different type of object)
# whenever you create an object in a database they need a primary key


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # unique =True means you can only have one email allowed in database
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
