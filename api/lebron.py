from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load LeBron career data
lebron_career_df = pd.read_csv('/Users/Jayden.Chen/vscode/csp/modeldata/lebron_career.csv')

@app.route('/get_lebron_stats', methods=['POST'])
def get_lebron_stats():
    # Get opponent from form data
    opponent = request.json.get('opponent')

    # Filter data for the specified opponent
    opponent_data = lebron_career_df[lebron_career_df['opp'] == opponent]

    # Get LeBron's last 10 matchups against the opponent
    last_10_games = opponent_data.tail(10)

    # Convert 'mp' to minutes
    def convert_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes

    last_10_games['mp'] = last_10_games['mp'].apply(convert_to_minutes)

    # Calculate rebounds as offensive and defensive combined
    last_10_games['rebounds'] = last_10_games['drb'] + last_10_games['orb']

    # Calculate field goal percentage
    last_10_games['fg_percentage'] = (last_10_games['fg'] / last_10_games['fga']) * 100

    # Calculate average stats for minutes played, points, assists, rebounds, steals, blocks, turnovers, and field goal percentage
    average_stats = last_10_games[['mp', 'pts', 'ast', 'rebounds', 'stl', 'blk', 'tov', 'fg_percentage']].mean()

    # Round average stats to the nearest tenth value
    average_stats_rounded = average_stats.round(1)

    # Convert average minutes played to hours
    average_minutes_played_hours = round(average_stats_rounded['mp'] / 60, 1)

    # Return the calculated stats
    return jsonify({
        'opponent': opponent,
        'average_minutes_played_hours': average_minutes_played_hours,
        'average_stats_rounded': average_stats_rounded.to_dict()
    })

if __name__ == '__main__':
    app.run(debug=True)
