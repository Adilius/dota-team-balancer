from itertools import combinations
from statistics import mean

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

players_numbers = [
     6000,
     5220,
    4820,
     4300,
    4100,
    3500,
    3300,
     2900,
     2700,
    2600
]

combinations = list(combinations(players,5))

for index, combination in enumerate(combinations):
    print(f'Matchup number: {index}')

    team_1_players = list(combination)
    team_1_ratings = [players[player] for player in team_1_players]
    team_1_mean = mean(team_1_ratings)
    print(f'Team 1 players: {team_1_players}')
    print(f'Team 1 ratings: {team_1_ratings}')
    print(f'Team 1 average: {team_1_mean}')

    team_2_players = [player for player in players.keys() if not player in combination]
    team_2_ratings = [players[player] for player in team_2_players]
    team_2_mean = mean(team_2_ratings)
    print(f'Team 2 players: {team_2_players}')
    print(f'Team 2 ratings: {team_2_ratings}')
    print(f'Team 2 average: {team_2_mean}')

    rating_advantage = abs(team_1_mean-team_2_mean)
    team_advantage = "1" if team_1_mean>team_2_mean else "2"

    print(f'Rating advantage: {rating_advantage} for team {team_advantage}')

    print('\n\n')

    #print(f'Average: {sum(combination)/len(combination)}')
#print(combinations)
print(f'Number of combinations: {len(combinations)}')
