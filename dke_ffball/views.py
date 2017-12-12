"""Views Module"""
from datetime import datetime
from flask import render_template
from dke_ffball import app

@app.route('/')
@app.route('/home')
def index():
    """Render the home page"""
    return render_template(
        'index.html',
        title='DKE Fantasy Football',
        year=datetime.now().year
        )