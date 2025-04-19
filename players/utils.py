import json
import os.path

import pandas as pd


def convert_to_json():
    all_player_stats_df = pd.read_csv('jupyter/all_player_stats.csv')
    all_player_stats_df.to_json('all_player_stats.json', orient='records', lines=False)
    league_averages_df = pd.read_csv('jupyter/league_averages.csv')
    league_averages_df.to_json('league_averages.json')


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


