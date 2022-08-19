from utils.custom_views import JsonMethodView
from utils.db_conn import Client
from http import HTTPStatus
from marshmallow import Schema, fields
from flask import request


class TeamLogo(JsonMethodView):

    class TeamLogoSchema(Schema):
        team_abr = fields.Str()

    def post(self):
        # Get the data from the request
        request_data = self.TeamLogoSchema().loads(request.data)
        db = Client()
        logo = db.cursor.execute(f"SELECT team_logo FROM logos WHERE team_abr = '{request_data.get('team_abr')}';")
        db.close_conn()

        team_logo_response = dict(team_logo_url=logo[0][0])

        return self.create_json_response(HTTPStatus.OK, team_logo_response)


class Teams(JsonMethodView):

    class Teams(Schema):
        team_abr_list = fields.List(fields.Str())

    def get(self):
        # Get the data from the request
        db = Client()
        teams = db.query(f"SELECT team_abr FROM logos;")
        db.close_conn()

        team_dict_response = {idx: team[0] for idx, team in enumerate(teams)}

        return self.create_json_response(HTTPStatus.OK, team_dict_response)

    def post(self):
        # Get the data from the request
        request_data = self.Teams().loads(request.data)
        team_list = request_data.get('team_abr_list')
        teams = tuple(team_list)

        db = Client()
        teams = db.query(query=f"SELECT team_abr FROM logos WHERE team_abr IN {teams};")
        db.close_conn()

        team_dict_response = {idx: team[0] for idx, team in enumerate(teams)}

        return self.create_json_response(HTTPStatus.OK, team_dict_response)
