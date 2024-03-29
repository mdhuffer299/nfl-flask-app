from utils.custom_views import JsonMethodView
from utils.db_conn import get_db_connection
import json
from http import HTTPStatus
from marshmallow import Schema, fields
from flask import request, render_template

class TeamLogo(JsonMethodView):

    class TeamLogoSchema(Schema):
        team_abr = fields.Str()

    def post(self):
        # Get the data from the request
        request_data = self.TeamLogoSchema().loads(request.data)
        db_conn = get_db_connection()
        cur = db_conn.cursor()
        cur.execute(f"SELECT team_logo FROM logos WHERE team_abr = '{request_data.get('team_abr')}';")
        logo = cur.fetchall()
        cur.close()
        db_conn.close()

        team_logo_response = dict(team_logo_url=logo[0][0])

        return self.create_json_response(HTTPStatus.OK, team_logo_response)


class Teams(JsonMethodView):

    class Teams(Schema):
        team_abr_list = fields.List(fields.Str())

    def get(self):
        # Get the data from the request
        db_conn = get_db_connection()
        cur = db_conn.cursor()
        cur.execute(f"SELECT team_abr FROM logos;")
        teams = cur.fetchall()
        cur.close()
        db_conn.close()

        team_dict_response = {idx: team[0] for idx, team in enumerate(teams)}

        return self.create_json_response(HTTPStatus.OK, team_dict_response)

    def post(self):
        # Get the data from the request
        request_data = self.Teams().loads(request.data)
        team_list = request_data.get('team_abr_list')
        teams = tuple(team_list)

        db_conn = get_db_connection()
        cur = db_conn.cursor()
        cur.execute(f"SELECT team_abr FROM logos WHERE team_abr IN {teams};")
        teams = cur.fetchall()
        cur.close()
        db_conn.close()

        team_dict_response = {idx: team[0] for idx, team in enumerate(teams)}

        return self.create_json_response(HTTPStatus.OK, team_dict_response)
