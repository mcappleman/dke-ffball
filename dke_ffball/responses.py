"""Consistent JSON repsonses for RESTful API"""
from flask import jsonify

def json_response(body, code):
    """
    Input a dict and a status code and return a jsonified response
    """
    response = jsonify(body)
    response.status_code = code
    return response
