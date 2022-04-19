from email.policy import default
from enum import unique
from sqlalchemy import PrimaryKeyConstraint
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
