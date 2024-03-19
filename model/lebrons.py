import pandas as pd
## Import and Train


# Replace 'path_to_your_csv_file' with the actual path where your CSV file is located
file_path = '/Users/Jayden.Chen/vscode/brawlbackend/static/assets/lebron_career.csv'

# Load the CSV file into a pandas DataFrame
lebron_career_df = pd.read_csv(file_path)
selected_columns = ['opp', 'mp', 'pts', 'fga', 'fgp', 'ast', 'orb', 'drb', 'stl', 'blk', 'tov']
lebron_career_cleaned = lebron_career_df[selected_columns].copy()

lebron_career_cleaned.dropna(inplace=True)


## Machine Learning

# Load LeBron career data
lebron_career_df = pd.read_csv('/Users/Jayden.Chen/vscode/csp/modeldata/lebron_career.csv')

# Select relevant columns
selected_columns = ['opp', 'mp', 'pts', 'ast', 'orb', 'drb', 'stl', 'blk', 'tov', 'fg', 'fga']

# Filter data for a specific opponent
def filter_opponent(data, opponent):
    return data[data['opp'] == opponent]

# Get LeBron's last 10 matchups against a specific opponent
def last_10_matchups(data):
    return data.tail(10)

# Ask for the opponent team
opponent = input("Enter the opponent team: ")

# Filter data for the specified opponent
opponent_data = filter_opponent(lebron_career_df, opponent)

# Get LeBron's last 10 matchups against the opponent
last_10_games = last_10_matchups(opponent_data)

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

# Print average stats
print("Average stats for the last 10 matchups against", opponent, ":")
print("Minutes played:", average_minutes_played_hours)
print("Points:", average_stats_rounded['pts'])
print("Field Goal Percentage:", average_stats_rounded['fg_percentage'])
print("Assists:", average_stats_rounded['ast'])
print("Rebounds:", average_stats_rounded['rebounds'])
print("Steals:", average_stats_rounded['stl'])
print("Blocks:", average_stats_rounded['blk'])
print("Turnovers:", average_stats_rounded['tov'])