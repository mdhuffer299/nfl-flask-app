from utils.custom_views import JsonMethodView
from utils.db_conn import Client
from http import HTTPStatus
from marshmallow import Schema, fields
from flask import request


class Games(JsonMethodView):

    class Games(Schema):
        season_year = fields.Int(required=True)
        week = fields.Int(required=True)
        away_team_abr = fields.Str(required=True)
        home_team_abr = fields.Str(required=True)

    def get(self):
        # Get the data from the request
        db = Client()
        games = db.query(f"SELECT * FROM games;")
        db.close_conn()

        game_dict_response = {idx: list(game) for idx, game in enumerate(games)}

        return self.create_json_response(HTTPStatus.OK, game_dict_response)

    def post(self):
        # Get the data from the request
        try:
            request_data = self.Games().loads(request.data)
        except:
            return self.create_json_response(HTTPStatus.BAD_REQUEST, f"Bad request, must more data")

        season_year = str(request_data['season_year'])
        week = request_data['week']
        away_team_abr = request_data['away_team_abr']
        home_team_abr = request_data['home_team_abr']

        game_id = f"{season_year}_{week}_{away_team_abr}_{home_team_abr}"

        db = Client()
        games = db.query(query=f"SELECT * FROM games WHERE game_id = '{game_id}';")
        db.close_conn()

        game_dict_response = {idx: list(game) for idx, game in enumerate(games)}

        return self.create_json_response(HTTPStatus.OK, game_dict_response)
