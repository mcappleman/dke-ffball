"""Imports"""
from flask import jsonify, request
from dke_ffball.models.Team import Team
from dke_ffball import app, db
from dke_ffball.errors import BadRequest
from dke_ffball.responses import json_response

@app.route('/api/team', methods=['GET'])
def get_all_teams():
    """Get all the teams from the database and return them as json"""
    teams = Team.query.all()

    body = {
        'message': 'Teams Found',
        'data': []
    }
    for team in teams:
        body['data'].append(team.to_dict())

    return json_response(body, 200)


@app.route('/api/team/<team_id>', methods=['GET'])
def get_team(team_id):
    """Get all the teams from the database and return them as json"""

    if team_id is None:
        raise BadRequest('No Team Id was supplied.', status_code=400)

    team = Team.query.filter_by(_id=team_id).first()

    body = {
        'message': 'Team Found',
        'data': team.to_dict()
    }
    return json_response(body, 200)


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

    body = {
        'message': '%s has been created' % (team.name),
        'data': team.to_dict()
    }
    return json_response(body, 201)


@app.route('/api/team/<team_id>', methods=['PUT'])
def update_team(team_id):
    """Get all the teams from the database and return them as json"""

    if team_id is None:
        raise BadRequest('No Team Id was supplied.', status_code=400)
    
    data = request.get_json()

    if data['name'] is None:
        raise BadRequest('You did not supply a team name.', status_code=400)
    
    team = Team.query.filter_by(_id=team_id).first()
    team.name = data['name']
    db.session.commit()

    body = {
        'message': '%s has been updated' % (team.name),
        'data': team.to_dict()
    }
    return json_response(body, 200)
