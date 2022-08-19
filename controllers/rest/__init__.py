from flask import Flask, Blueprint
from controllers.rest.teams import TeamLogo, Teams
from controllers.rest.games import Games


def create_rest_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    rest_blueprint = Blueprint('rest', __name__,
                               url_prefix='/rest',
                               template_folder='../../templates')

    team_logo = TeamLogo.as_view('team_logo')
    rest_blueprint.add_url_rule('/team/logo',
                                view_func=team_logo,
                                methods=['POST'])

    teams = Teams.as_view('teams')
    rest_blueprint.add_url_rule('/teams',
                                view_func=teams,
                                methods=['GET', 'POST'])

    games = Games.as_view('games')
    rest_blueprint.add_url_rule('/games',
                                view_func=games,
                                methods=['GET', 'POST'])

    app.register_blueprint(rest_blueprint, url_prefix="/rest")

    return app
