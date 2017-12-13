"""Game Model Module"""
from dke_ffball import db
from dke_ffball.models import BaseModel

class Game(BaseModel, db.Model):
    """Game Class that will model the games table in the database"""

    __tablename__ = 'games'

    _id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    week = db.Column(db.Integer)

    def __init__(self, year, week):
        BaseModel.__init__(self)
        self.year = year
        self.week = week


    def __repr__(self):
        return '<Game %s, %s, id %s' % (self.year, self.week, self._id)
