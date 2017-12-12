"""Imports"""
from os import environ
from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from controllers import TeamController

app = Flask(__name__)
app.config.from_object(environ.get('APP_SETTINGS', 'config.DevelopmentConfig'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def index():
    """Render the home page"""
    return render_template(
        'index.html',
        title='DKE Fantasy Football',
        year=datetime.now().year
        )


if __name__ == '__main__':
    app.run()
