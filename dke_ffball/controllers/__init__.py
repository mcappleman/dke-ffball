"""Base Controller Module"""
from flask import jsonify
from dke_ffball import app

@app.route('/api')
def base_api():
    """Base api route"""
    return jsonify(
        status=200,
        message='You have hit the dke fantasy api.'
        )
