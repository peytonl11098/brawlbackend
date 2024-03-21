""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

import pandas as pd
class LebronStatsPredict:
    def __init__(self, opp):
        self.opp = opp

    def predict(self):
        # Load LeBron career data
        file_path = 'static/assets/lebron_career.csv'
        lebron_career_df = pd.read_csv(file_path)

        # Filter data for the specified opponent
        opponent_data = lebron_career_df[lebron_career_df['opp'] == self.opp]

        # Get LeBron's last 10 matchups against the opponent
        last_10_games = opponent_data.tail(10)

        # Convert 'mp' to minutes
        last_10_games['mp'] = last_10_games['mp'].apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]))

        # Calculate rebounds as offensive and defensive combined
        last_10_games['rebounds'] = last_10_games['drb'] + last_10_games['orb']

        # Calculate field goal percentage
        last_10_games['fg_percentage'] = (last_10_games['fg'] / last_10_games['fga']) * 100

        # Calculate average stats for minutes played, points, assists, rebounds, steals, blocks, turnovers, and field goal percentage
        average_stats = last_10_games[['mp', 'pts', 'ast', 'rebounds', 'stl', 'blk', 'tov', 'fg_percentage']].mean()
        average_stats_rounded = average_stats.round(1)

        return {
            'opponent': self.opp,
            'average_minutes_played_hours': round(average_stats_rounded['mp'] / 60, 1),
            'average_stats_rounded': average_stats_rounded.to_dict()
        }

def initLebron(opp):
    # Load LeBron career data
    file_path = '/static/assets/lebron_career.csv'
    lebron_career_df = pd.read_csv(file_path)

    # Filter data for the specified opponent
    opponent_data = lebron_career_df[lebron_career_df['opp'] == opp]

    # Get LeBron's last 10 matchups against the opponent
    last_10_games = opponent_data.tail(10)

    # Convert 'mp' to minutes
    last_10_games['mp'] = last_10_games['mp'].apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]))

    # Calculate rebounds as offensive and defensive combined
    last_10_games['rebounds'] = last_10_games['drb'] + last_10_games['orb']

    # Calculate field goal percentage
    last_10_games['fg_percentage'] = (last_10_games['fg'] / last_10_games['fga']) * 100

    # Calculate average stats for minutes played, points, assists, rebounds, steals, blocks, turnovers, and field goal percentage
    average_stats = last_10_games[['mp', 'pts', 'ast', 'rebounds', 'stl', 'blk', 'tov', 'fg_percentage']].mean()
    average_stats_rounded = average_stats.round(1)

    return {
        'opponent': opp,
        'average_minutes_played_hours': round(average_stats_rounded['mp'] / 60, 1),
        'average_stats_rounded': average_stats_rounded.to_dict()
    }
