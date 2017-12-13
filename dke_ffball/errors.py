"""Error Handlers module"""
from flask import jsonify
from dke_ffball import app

class BadRequest(Exception):
    """Bad Request Error class"""
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload


    def to_dict(self):
        """Error to Dictionary"""
        res_dict = dict(self.payload or ())
        res_dict['message'] = self.message
        res_dict['status'] = self.status_code
        return res_dict


@app.errorhandler(BadRequest)
def handle_bad_requests(error):
    """Error Handler for bad requests"""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
