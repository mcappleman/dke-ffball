"""Imports"""
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dke_ffball.models.Team import Team
from dke_ffball import app, db
from dke_ffball.errors import BadRequest


@app.route('/api/team', methods=['GET'])
def get_all_teams():
    """Get all the teams from the database and return them as json"""
    teams = Team.query.all()
    return jsonify(
        status=200,
        message='Got the teams',
        data=teams
        )


@app.route('/api/team/<team_id>', methods=['GET'])
def get_team(team_id):
    """Get all the teams from the database and return them as json"""

    if team_id is None:
        raise BadRequest('No Team Id was supplied', status_code=400)

    team = Team.query.filter_by(_id=team_id).first()
    return jsonify(
        status=200,
        message='Got the team',
        data=team
        )


@app.route('/api/team', methods=['POST'])
def add_team():
    """Add a team to the database"""
    data = request.get_json()
    name = data['name']

    if name is None:
        raise BadRequest('You did not supply a team name.', status_code=400)

    duplicate = Team.query.filter_by(name=name).first()
    if duplicate is not None:
        raise BadRequest('This team has already been created.', status_code=400)

    team = Team(
        name=name
    )
    db.session.add(team)
    db.session.commit()
    return jsonify(
        status=201,
        message='%s has been created' % (team.name),
        data=team
    )


@app.route('/api/team/<team_id>', methods=['PUT'])
def update_team(team_id):
    """Get all the teams from the database and return them as json"""

    if team_id is None:
        raise BadRequest('No Team Id was supplied', status_code=400)
    
    data = request.get_json()

    if data['name'] is None:
        raise BadRequest('No team Name was supplied', status_code=400)
    
    team = Team.query.filter_by(_id=team_id).first()
    team.name = data['name']
    db.session.commit()
    return jsonify(
        status=200,
        message='Updated the team',
        data=team
        )
