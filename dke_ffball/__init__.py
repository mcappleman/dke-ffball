"""Imports"""
from os import environ
from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(environ.get('APP_SETTINGS', 'config.DevelopmentConfig'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import dke_ffball.errors
import dke_ffball.views
import dke_ffball.controllers
import dke_ffball.controllers.TeamController
