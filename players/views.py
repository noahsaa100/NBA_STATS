from flask import Blueprint, render_template, request, json
import pandas as pd

from players.utils import get_player_data, load_player_data, get_league_data

players_bp = Blueprint('players', __name__)


@players_bp.route('/')
def index():
    return render_template("index.html")


@players_bp.route('/compare', methods=['GET', 'POST'])
def compare():
    players = load_player_data()  # Load all player data
    player_stats = []
    league_averages = None

    if request.method == 'POST':
        selected_players = request.form.getlist('players')

        # Get player data for selected players
        player_stats = [get_player_data(player) for player in selected_players if get_player_data(player)]

        # Get league data for the season of the first selected player
        if player_stats:
            if len (player_stats)== 1:
                league_averages = get_league_data(player_stats[0]["Year"])

    return render_template("compare.html", players=players, player_stats=player_stats, league_averages=league_averages)


@players_bp.route('/profile/<player_name>', methods=['GET'])
def player_profile(player_name):
    player_data = get_player_data(player_name)

    if player_data is None:
        return "Player not found", 404

    return render_template('player_profile.html', player=player_data)
