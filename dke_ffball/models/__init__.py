"""Imports"""
from datetime import datetime
from dke_ffball import db

class BaseModel(db.Model):
    """Base Model to be extended by every model"""
    __abstract__ = True

    def __init__(self, *args):
        pass


    def __repr__(self):
        """Define a base way to print models"""
        pass


    def to_dict(self):
        """Define a base way to jsonify models"""
        pass
