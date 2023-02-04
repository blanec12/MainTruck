from enum import unique
from flask_login import UserMixin
from db.config import db
import uuid as uuid_pkg

class Users(UserMixin, db.Model):
    id  = db.Column(db.String(255), primary_key=True, default=uuid_pkg.uuid4)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(100))
    createdByID = db.Column(db.String(255))
    createdDateTime = db.Column(db.DateTime)
    lastModifiedByID = db.Column(db.String(255))
    lastModifiedDateTime = db.Column(db.DateTime)
    isAdmin = db.Column(db.Integer)