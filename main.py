import itertools
import numpy as np
import pandas as pd
from tabulate import tabulate


class League:
    def __init__(self):
        self.teams = []  # Create teams list

    # Add team to teams list
    def add_team(self, team):
        self.teams.append(team)

        # Playing a single match

    def play_match(self, team_A, team_B):
        if team_A.team_strength() > team_B.team_strength():
            g_A = max(0, np.random.normal(3, 1))
            g_B = max(0, np.random.normal(1.5, 1))
        elif team_A.team_strength() == team_B.team_strength():
            g_A = max(0, np.random.normal(2, 1))
            g_B = max(0, np.random.normal(2, 1))
        else:
            g_A = max(0, np.random.normal(1.5, 1))
            g_B = max(0, np.random.normal(3, 1))

        goals_A = int(round(g_A))
        goals_B = int(round(g_B))

        return goals_A, goals_B

    # Playing a league season for n teams in self.teams
    def simulate_season(self):
        # 1. Generate all home and away matches using itertools.permutations
        fixtures = list(itertools.permutations(self.teams, 2))  # nCk where k=2

        # 2. Simulate each match
        for team_A, team_B in fixtures:
            goals_A, goals_B = self.play_match(team_A, team_B)

            # 3. Update league table
            # Wins, draws, losses, points
            if goals_A > goals_B:
                team_A.wins += 1
                team_B.losses += 1
                team_A.points += 3
            if goals_A == goals_B:
                team_A.draws += 1
                team_B.draws += 1
                team_A.points += 1
                team_B.points += 1
            if goals_A < goals_B:
                team_A.losses += 1
                team_B.wins += 1
                team_B.points += 3

            # Goals for, goals against
            team_A.goals_for += goals_A
            team_B.goals_for += goals_B
            team_A.goals_against += goals_B
            team_B.goals_against += goals_A

        # 3. Produce the league table using Pandas from dictionaries
        table_data = []
        for team in self.teams:
            table_data.append({"Team": team.name, "PLAYED": team.wins + team.draws + team.losses,
                               "W": team.wins, "D": team.draws, "L": team.losses,
                               "GF": team.goals_for, "GA": team.goals_against,
                               "GD": team.goals_for - team.goals_against, "PTS": team.points})
        df = pd.DataFrame(table_data)

        # Sort the DataFrame by points and then goal difference, both descending
        df = df.sort_values(by=["PTS", "GD"], ascending=[False, False]).reset_index(drop=True)

        # Increase the index by 1 to reflect the positions
        df.index = df.index + 1

        # 4. Use tabulate to enhance output
        final_table = tabulate(df, headers="keys", tablefmt="fancy_grid", showindex=True)

        # 5. Return the final league table
        return final_table


class Team:
    def __init__(self, name, level, injuries):
        self.name = name
        self.level = level
        self.injuries = injuries
        self.__luck = np.random.randint(1, 10)  # demonstration of encapsulation
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0

    # Dunder method for printing out team attributes
    def __str__(self):
        return f"{self.name}: level - {self.level}, injuries - {self.injuries}"

    # Establish how strong a team is from their level, injuries and luck
    def team_strength(self):
        return self.level - self.injuries * 0.2 + self.__luck * 0.2


# Setting up the teams
man_city = Team("Man City", 10, 7)
arsenal = Team("Arsenal", 8, 4)
liverpool = Team("Liverpool", 7, 1)
man_utd = Team("Man Utd", 6, 4)

# Playing a league
prem = League()
prem.add_team(man_city)
prem.add_team(arsenal)
prem.add_team(liverpool)
prem.add_team(man_utd)

print("⚽ Welcome to the Football Simulator! ⚽\n")
print(prem.simulate_season())
