from flask import Blueprint, render_template, request, json
import pandas as pd


players_bp = Blueprint('players', __name__)

averages_df = pd.read_csv('data/averages.csv')
league_averages_df = pd.read_csv('data/league_averages.csv')
totals_df = pd.read_csv('data/totals.csv')
all_player_stats_df = pd.read_csv('data/all_player_stats.csv')
all_player_stats_df.to_json('all_player_stats.json', orient='records', lines=False)
totals_df.to_json('totals.json', orient='records', lines=False)


@players_bp.route('/')
def index():
    return render_template("index.html")


@players_bp.route('/compare', methods=['GET', 'POST'])
def compare():
    players = averages_df["Player"].unique()
    player_stats = None
    league_averages = league_averages_df.iloc[0].to_dict()

    if request.method == 'POST':
        selected_players = request.form.getlist('players')
        player_stats = averages_df[averages_df["Player"].isin(selected_players)]

    return render_template("compare.html")


@players_bp.route('/profile/<player_name>', methods=['GET'])
def player_profile(player_name):
    # Load the JSON data
    with open('all_player_stats.json') as f:
        data = json.load(f)

    # Find the player in the data
    player_data = next((player for player in data if player['Player'] == player_name), None)

    # If the player is not found, return a 404 or an error page
    if player_data is None:
        return "Player not found", 404

    return render_template('player_profile.html', player=player_data)
