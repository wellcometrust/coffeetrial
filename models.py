from app import db
from datetime import datetime


class Match(db.Model):

    def __init__(self, user_1, user_2, round):
        self.user_1 = user_1
        self.user_2 = user_2
        self.round = round

    __tablename__ = "match"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_1 = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_2 = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    round = db.Column(db.Integer, db.ForeignKey('round.id'), nullable=False)


class User(db.Model):

    def __init__(self, firstname, lastname, email,
                 active, joined, department_id):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.active = active
        self.joined = joined
        self.department_id = department_id

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(128), nullable=False)
    lastname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    joined = db.Column(db.DateTime(), default=datetime.now())
    department_id = db.Column(
        db.Integer,
        db.ForeignKey('department.id'),
        nullable=False
    )


class Department(db.Model):

    def __init__(self, name):
        self.name = name

    __tablename__ = "department"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)


class Round(db.Model):

    def __init__(self, date):
        self.date = date

    __tablename__ = "round"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(), nullable=False)
