# database model for a note
from . import db  # from this package in this db
from flask_login import UserMixin  # custom class for user
from sqlalchemy.sql import func

# Note Model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # ForeignKey


# User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # primary key
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')  # relationship use Cap
