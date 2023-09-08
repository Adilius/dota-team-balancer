from itertools import combinations
from statistics import mean
import json
from collections import OrderedDict


# Mockup data - Player name : Player rating
players = {
    "Alpha": 6000, 
    "Bravo": 5220,
    "Charlie": 4820,
    "Delta": 4300,
    "Echo": 4100,
    "Foxtrot": 3500,
    "Golf": 3300,
    "Hotel": 2900,
    "India": 2700,
    "Juliett": 2600,
}

# Get all subsets of combinations with 5 items from a set of 10 players
combinations = list(combinations(players,5))

# Get only combinations which player 1 is present (removes inverse combinations which leads to duplicate matchups)
unique_combinations = list()
for combination in combinations:
    if next(iter(players)) in combination:
        unique_combinations.append(combination)
combinations = unique_combinations

# Store unique matchups
matchups = dict()

# Create matchup data
for index, combination in enumerate(combinations):
    
    # Create unique matchup index
    matchup_number = index

    # Team 1
    team_1_players = list(combination)
    team_1_ratings = [players[player] for player in team_1_players]
    team_1_mean = mean(team_1_ratings)

    # Team 2
    team_2_players = [player for player in players.keys() if not player in combination]
    team_2_ratings = [players[player] for player in team_2_players]
    team_2_mean = mean(team_2_ratings)

    # Team advantage
    rating_advantage = abs(team_1_mean-team_2_mean)
    team_advantage = "1" if team_1_mean>team_2_mean else "2"

    # Create dict for matchup
    matchup = {
        matchup_number : {

        
        "Rating advantage" : rating_advantage,
        "Team advantage" : team_advantage,
        "Team 1" : {

            "Players": team_1_players,
            "Ratings": team_1_ratings,
            "Average rating": team_1_mean
        },
        "Team 2" : {

            "Players": team_2_players,
            "Ratings": team_2_ratings,
            "Average rating": team_2_mean
        }
    }
    }
    matchups.update(matchup)

# Sort matchups depending on rating advantage
sorted_matchups = OrderedDict(sorted(matchups.items(), key=lambda x: x[1]['Rating advantage']))


# Print matchup information
print(json.dumps(sorted_matchups, indent=4))
print(f'Number of combinations: {len(combinations)}')
