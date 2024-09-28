import random
import pdb

# Define teams and divisions
divisions = {
    "A": ["A1", "A2", "A3"],
    "B": ["B1", "B2", "B3"],
    "C": ["C1", "C2", "C3"],
    "D": ["D1", "D2", "D3"]
}

# Generate all intra-division matchups (3 matches per team)

intra_division_games = []
for division, teams in divisions.items():
    intra_division_games += [
        (teams[0], teams[1]), (teams[1], teams[0]), (teams[0], teams[1]),  # A1 vs A2 (twice home/away)
        (teams[0], teams[2]), (teams[2], teams[0]), (teams[0], teams[2]),  # A1 vs A3 (twice home/away)
        (teams[1], teams[2]), (teams[2], teams[1]), (teams[1], teams[2])   # A2 vs A3 (twice home/away)
    ]

# Generate all inter-division matchups (each team plays twice with every team outside its division)
inter_division_games = []
div_list = list(divisions.values())

# Loop over each division and generate games against all teams outside the division
for i in range(4):
    for j in range(i+1, 4):
        for team1 in div_list[i]:
            for team2 in div_list[j]:
                inter_division_games.append((team1, team2))  # Home game for team1
                inter_division_games.append((team2, team1))  # Away game for team1

# Shuffle games to randomize scheduling
random.shuffle(intra_division_games)
random.shuffle(inter_division_games)

# Combine intra and inter-division games, distributing them over 24 weeks
total_weeks = 24
games_per_week = 6  # Each week has 6 games to ensure all 12 teams play

schedule = [[] for _ in range(total_weeks)]

# First, place all intra-division games
for i in range(len(intra_division_games)):
    for weekIndex in range(0,total_weeks):
        schedule[weekIndex].append(intra_division_games[i])



# Then, place inter-division games
for i in range(len(inter_division_games)):
    for weekIndex in range(0,total_weeks):
        schedule[weekIndex].append(inter_division_games[i])


# Ensure no team plays twice in one week
#def team_in_week(week_games, team):
#    return any(team in game for game in week_games)

schedule_nodup = [[] for _ in range(total_weeks)]


# Adjust games to prevent the same team playing twice in the same week
weekIndex = 0
for week in schedule:
    week_teams = set()
    pdb.set_trace()
    for game in week:
        team1, team2 = game
        hasConflict = False
        if team1 in week_teams :
            print(f"Conflict: {team1} already scheduled this week!")
            hasConflict = True
            # remove the game
        else:
            week_teams.add(team1)

        if  team2 in week_teams:
            print(f"Conflict:{team2} already scheduled this week!")
            hasConflict = True
            # remove the game
        else:
            week_teams.add(team2)

        if (hasConflict == False):
            schedule_nodup[weekIndex].append(game)


    weekIndex = weekIndex +1


pdb.set_trace()


# Print the schedule
for week_num, week in enumerate(schedule, start=1):
    print(f"Week {week_num}:")
    for game in week:
        print(f"{game[0]} vs {game[1]}")
    print()
