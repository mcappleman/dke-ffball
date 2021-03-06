"""Imports"""
from flask import jsonify
from dke_ffball import db
from dke_ffball.models import BaseModel


class Team(BaseModel, db.Model):
    """Team model to store the teams in the database"""

    __tablename__ = 'teams'

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())


    def __init__(self, name):
        BaseModel.__init__(self)
        self.name = name


    def __repr__(self):
        return '<Team %s, id %s' % (self.name, self._id)


    def to_dict(self):
        data = {
            'id': self._id,
            'name': self.name
        }
        return data
