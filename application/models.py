from application import db
from sqlalchemy.orm import backref
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    wells = db.relationship('Well', backref=backref('user'))

class Well(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    data = db.relationship('Data', backref=backref('well'))

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    well_id = db.Column(db.Integer, db.ForeignKey('well.id'))

    min = db.Column(db.Integer)
    gas = db.Column(db.Integer)
    oil = db.Column(db.Integer)
    water = db.Column(db.Integer)
