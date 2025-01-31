import json
import pandas as pd


def convert_to_json():
    all_player_stats_df = pd.read_csv('data/all_player_stats.csv')
    all_player_stats_df.to_json('all_player_stats.json', orient='records', lines=False)


def load_player_data():
    with open('all_player_stats.json') as f:
        return json.load(f)


def get_player_data(player_name):
    data = load_player_data()
    return next((player for player in data if player['Player'] == player_name), None)