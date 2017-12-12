"""Imports"""
import datetime
from app import db

class BaseModel(db.Model):
    """Base Model to be extended by every model"""
    __abstract__ = True

    def __init__(self, *args):
        pass


    def __repr__(self):
        """Define a base way to print models"""
        return '%s%s' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
            })


    def json(self):
        """Define a base way to jsonify models"""
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
            }
