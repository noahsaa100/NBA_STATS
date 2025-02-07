import json
import os.path

import pandas as pd


def convert_to_json():

    if not os.path.exists('all_player_stats.json'):
        all_player_stats_df = pd.read_csv('data/all_player_stats.csv')
        all_player_stats_df.to_json('all_player_stats.json', orient='records', lines=False)


    if not os.path.exists('league_averages.json'):
        league_averages_df = pd.read_csv('data/league_averages.csv')
        league_averages_df.to_json('league_averages.json', orient='records', lines=False)


def load_player_data():
    with open('all_player_stats.json') as f:
        return json.load(f)


def load_league_data():
    with open('league_averages.json') as f:
        return json.load(f)


def get_player_data(player_name):
    data = load_player_data()
    return next((player for player in data if player['Player'] == player_name), None)


def get_league_data(year):
    data = load_league_data()
    return next ((entry for entry in data if entry['Year'] == year))


