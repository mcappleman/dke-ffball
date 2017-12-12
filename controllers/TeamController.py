"""Imports"""
from app import app, db
from flask import jsonify, request
from models.Team import Team
from controllers import BaseController

class TeamController(BaseController):
    """Team Controller to handle the team routes"""

    def __init__(self):
        BaseController.__init__(self)


    @app.route('/api/team', methods=['GET'])
    def get_all_teams(self):
        """Get all the teams from the database and return them as json"""
        teams = db.session.query(Team).all()
        return jsonify(
            status=200,
            message='Got the teams',
            data=teams
            )

    @app.route('/api/team', methods=['POST'])
    def add_team(self):
        data = request.get_json()
        name = data['name']
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
        
