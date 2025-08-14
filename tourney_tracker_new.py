import pandas as pd
# import openpyxl
import os



class Player:
    def __init__(self, name):
        """
        Initialize a Player instance with the given name.

        Parameters:
        - name (str): The name of the player.
        """
        self.name = name
        self.sinks = 0
        self.mugs = 0
        self.lows = 0
        self.highs = 0
        self.drops = 0
        self.balls_back = 0
        self.catches = 0
        self.offs = 0
        self.tosses = 0
        self.points = 0
        self.wins = 0
        self.games = 0

    def set_item(self, var, val):
        """
        Set the value of a specific attribute for the player.

        Parameters:
        - var (str): The attribute name.
        - val: The value to be set for the attribute.
        """
        setattr(self, var, val)

    def get_item(self, var):
        """
        Get the value of a specific attribute for the player.

        Parameters:
        - var (str): The attribute name.

        Returns:
        The value of the specified attribute.
        """
        return getattr(self, var)

    def reset_stats(self):
        """
        Reset all statistics of the player to zero.
        """
        self.sinks = 0
        self.mugs = 0
        self.lows = 0
        self.highs = 0
        self.drops = 0
        self.balls_back = 0
        self.catches = 0
        self.offs = 0
        self.tosses = 0
        self.points = 0
        self.wins = 0
        self.games = 0

    def update_stats(self, result, player_dict, other = None):
        """
        Update the player's statistics based on the result of a toss.

        Parameters:
        - result (str): The result of the toss.
        - player_dict (dict): Dictionary containing player instances.
        - other (str, optional): Player name relevant to the result (used in catch or drop). Defaults to None.

        Note:
        - This method increments the toss count for the player.
        - If the result is a catch or drop, it prompts for the other player's name (if not provided).
        - Updates relevant statistics based on the toss result, incrementing points for specific outcomes.
        """
        if result != "wins" and result != "games":
            self.tosses += 1

        if result == "catches":
            player_dict[other].catches += 1
        elif result == "drops":
            player_dict[other].drops += 1
            self.points += 1
        elif result != "nothing":
            setattr(self, result, getattr(self, result) + 1)
            if result in {"sinks", "mugs", "balls_back"}:
                self.points += 1

    def calculate_metrics(self):
        """
        Calculate two metrics related to player performance.

        Returns:
        Tuple containing:
        - points_per_toss (float): Average points per toss.
        - catches_per_drop (float): Average catches per drop.
        """
        if self.tosses == 0:
            points_per_toss = float("inf")
        else:
            points_per_toss = self.points / self.tosses
        if self.drops == 0:
            catches_per_drop = float("inf")
        else:
            catches_per_drop = self.catches / self.drops
        return points_per_toss, catches_per_drop

    def get_stats(self):
        """
        Get a dictionary containing the player's statistics.

        Returns:
        Dictionary with statistics keys and corresponding values.
        """
        return {
            "tosses": self.tosses,
            "sinks": self.sinks,
            "mugs": self.mugs,
            "lows": self.lows,
            "highs": self.highs,
            "longs/sides": self.offs,
            "balls back": self.balls_back,
            "catches": self.catches,
            "drops": self.drops,
            "points": self.points,
            "wins": self.wins,
            "games": self.games,
        }


# Mapping dictionary for toss outcomes
mapping = {
    "s": "sinks",
    "m": "mugs",
    "l": "lows",
    "h": "highs",
    "d": "drops",
    "b": "balls_back",
    "c": "catches",
    "o": "offs",  # long/side
    "n": "nothing",
    "u": "undo last toss",
}


def create_teams(teams = {}, player_dict = {}):
    """
    Creates teams and initializes player statistics.

    Parameters:
    - teams (dict, optional): Existing teams dictionary. Defaults to an empty dictionary.
    - player_dict (dict, optional): Existing player dictionary. Defaults to an empty dictionary.

    Returns:
    Tuple containing:
    - teams (dict): Dictionary with team numbers as keys and player pairs as values.
    - player_dict (dict): Dictionary with player names as keys and player objects as values.
    """

    if not teams:
        # If no existing teams, prompt for the number of teams playing
        num_teams = int(input("Number of teams playing: "))
        for i in range(num_teams):
            player_1 = input(f"Player 1 for Team {i + 1}: ")
            player_dict[player_1] = Player(player_1)

            player_2 = input(f"Player 2 for Team {i + 1}: ")
            player_dict[player_2] = Player(player_2)

            teams[i + 1] = [player_1, player_2]
    else:
        # If existing teams, prompt for additional teams
        num_teams = int(input("Number of teams being added: "))
        n = len(teams)
        for i in range(n+1, n+1+num_teams):
            player_1 = input(f"Player 1 for Team {i}: ")
            player_dict[player_1] = Player(player_1)

            player_2 = input(f"Player 2 for Team {i}: ")
            player_dict[player_2] = Player(player_2)

            teams[i] = [player_1, player_2]

    return teams, player_dict


def game(team_1, team_2, player_dict):
    """
    Simulate a game between two teams.

    Parameters:
    - team_1 (list): List of player names for the first team.
    - team_2 (list): List of player names for the second team.
    - player_dict (dict): Dictionary containing player instances.

    Returns:
    Tuple containing:
    - winner (list): List of winning team's player names.
    - score (list): List containing scores for each team.
    - player_dict (dict): Updated dictionary with player statistics.
    """
    score = [0, 0]
    first_toss = True
    toss_num = 0
    tracker = []  # To keep track of tosses

    while True:
        # Input handling for the first toss
        while first_toss:
            first_player = input("First toss is by: ")
            if first_player not in team_1 and first_player not in team_2:
                print("\nError: Player not in team 1 or team 2")
                print(f"Team 1: {team_1}, Team 2: {team_2}\n")
                continue
            if first_player in team_1:
                first_team = 0
                if team_1[0] == first_player:
                    third_player = team_1[1]
                else:
                    third_player = team_1[0]
            else:
                first_team = 1
                if team_2[0] == first_player:
                    third_player = team_2[1]
                else:
                    third_player = team_2[0]

            second_player = input("Second toss is by: ")
            if second_player not in team_1 and second_player not in team_2:
                print("\nError: Player not in team 1 or team 2")
                print(f"Team 1: {team_1}, Team 2: {team_2}\n")
                continue
            if second_player in team_1:
                second_team = 0
                if team_1[0] == second_player:
                    fourth_player = team_1[1]
                else:
                    fourth_player = team_1[0]
            else:
                second_team = 1
                if team_2[0] == second_player:
                    fourth_player = team_2[1]
                else:
                    fourth_player = team_2[0]
            if second_team == first_team:
                print("\nError: Players on same team")
                print(f"Team 1: {team_1}, Team 2: {team_2}\n")
                continue
            print("\n" * 3)
            first_toss = False

        # Check and display the current score
        print(f"Score: {team_1} - {score[0]} {team_2} - {score[1]}\n")

        # Check score to see if game should be over
        is_over, winner = game_over(score, team_1, team_2)
        if is_over:
            for i in winner:
                player_dict[i].update_stats("wins", player_dict)
            break

        # Determine the player and team for the current toss
        if toss_num % 4 == 0:
            player = first_player
            team_num = first_team
        elif toss_num % 4 == 1:
            player = second_player
            team_num = second_team
        elif toss_num % 4 == 2:
            player = third_player
            team_num = first_team
        else:
            player = fourth_player
            team_num = second_team

        # Determine opposing team for current toss
        if team_num == 0:
            # cur_team = team_1
            other_team = team_2
        else:
            # cur_team = team_2
            other_team = team_1

        # Display current player and mapping options
        print(f"Tossing: {player}")
        print(mapping)
        print("Type cancel to end game and void all recorded stats")

        # Get the result of the toss from user input
        result = input("Result of toss: ")

        # Input validation loop
        while result not in mapping:
            if result == "cancel":
                tracker = []  # Reset tracker if the game is canceled
                return None, None, player_dict
            print("\nError: Input not an option\n")
            print(f"Score: {team_1} - {score[0]} {team_2} - {score[1]}\n")
            print(f"Tossing: {player}")
            print(mapping)
            result = input("Result of toss: ")

        # Map the result and update the tracker
        out = mapping[result]
        if out == "undo last toss":
            print('\n\n')
            if tracker:
                prev_player, prev_result, prev_op = tracker.pop()
                if prev_result == "balls_back":
                    score[team_num] -= 1
                    continue
                if prev_result in ["sinks", "mugs", "drops"]:
                    if team_num == 0:
                        score[1] -= 1
                    else:
                        score[0] -= 1
                toss_num -= 1
                continue
            print("\nError: No tosses have been recorded\n")
            continue
        elif out == "drops":
            while True:
                dropping = input("Player that dropped the die: ")
                if dropping not in player_dict:
                    print("Error: player input not valid \n")
                    print(f"Other team: {other_team} \n")
                elif dropping not in other_team:
                    print("Error: Player not on other team")
                    print(f"Other team: {other_team} \n")
                else:
                    tracker.append((player, out, dropping))
                    break
        elif out == "catches":
            while True:
                catching = input("Player that caught the die: ")
                if catching not in player_dict:
                    print("Error: player input not valid \n")
                    print(f"Other team: {other_team} \n")
                elif catching not in other_team:
                    print("Error: Player not on other team")
                    print(f"Other team: {other_team} \n")
                else:
                    tracker.append((player, out, catching))
                    break
        else:
            tracker.append((player, out, None))

        # Update the score based on the toss result
        if out in ["sinks", "mugs", "drops", "balls_back"]:
            score[team_num] += 1

        print("\n\n")
        if out != "balls_back":
            toss_num += 1

    # Update player statistics based on the tracked tosses
    for p, r, op in tracker:
        player_dict[p].update_stats(r, player_dict, op)
    
    for player_id in [first_player, second_player, third_player, fourth_player]:
        player_dict[player_id].update_stats("games", player_dict)

    return winner, score, player_dict


def game_over(score, team_1, team_2):
    """
    Check if the game is over based on the current score.

    Parameters:
    - score (list): List containing scores for each team.
    - team_1 (list): List of player names for the first team.
    - team_2 (list): List of player names for the second team.

    Returns:
    Tuple containing:
    - is_over (bool): True if the game is over, False otherwise.
    - winner (list): List of winning team's player names, or None if the game is not over.
    """
    if (score[0] == 7 and score[1] <= 5) or (
        score[0] >= 6 and score[1] >= 6 and score[0] - score[1] == 2
    ):
        return True, team_1
    if (score[1] == 7 and score[0] <= 5) or (
        score[0] >= 6 and score[1] >= 6 and score[1] - score[0] == 2
    ):
        return True, team_2
    return False, None


if __name__ == "__main__":
    filename = "snappa_tourney.csv"
    if os.path.exists(filename):
        season_df = pd.read_csv(filename, index_col="Player Name")
    else:
        season_df = pd.DataFrame()

    teams, player_dict = create_teams()

    while True:
        if len(teams) == 2:
            matchup_1 = teams[1]
            matchup_2 = teams[2]
        else:
            while True:
                player_1 = input("One player on team 1: ")
                player_2 = input("One player on team 2: ")
                test_1 = False
                test_2 = False
                for key in teams:
                    if player_1 in teams[key]:
                        if not test_1:
                            matchup_1 = teams[key]
                            player1_test = input(f"Is this the correct team? {matchup_1} y/n\n")
                            if player1_test == "y":
                                test_1 = True
                    if player_2 in teams[key]:
                        if not test_2:
                            matchup_2 = teams[key]
                            player2_test = input(f"Is this the correct team? {matchup_2} y/n\n")
                            if player2_test == "y":
                                test_2 = True
                if not test_1:
                    print(f"Error: Player 1 - {player_1} - not in teams")
                    inp = input("Add a team? y/n \n")
                    if inp == "y":
                        teams, player_dict = create_teams(teams, player_dict)
                    continue
                if not test_2:
                    print(f"Error: Player 2 - {player_2} - not in teams")
                    inp = input("Add a team? y/n \n")
                    if inp == "y":
                        teams, player_dict = create_teams(teams, player_dict)
                    continue
                if matchup_1 == matchup_2:
                    print("Error: Players on same team.")
                    print(matchup_1)
                    print()
                else:
                    break

        winner, score, player_dict = game(matchup_1, matchup_2, player_dict)

        if winner is not None:
            print(f"Winner: {winner[0]} + {winner[1]}")
            print(f"Score: {score[0]} - {score[1]}")

        test = input("Type n for the next game. Type a to add teams. Type f to finish. ")
        if test == "a":
            teams, player_dict = create_teams(teams, player_dict)
        if test == "f":
            break

    # Creating DataFrame with "Player Name" as index
    data = {
        player_name: player.get_stats() for player_name, player in player_dict.items()
    }
    game_df = pd.DataFrame.from_dict(data, orient="index")
    game_df.index.name = "Player Name"  # Set the index name

    def combine_dfs(season_df, game_df):
        if season_df.empty:
            return game_df

        season_df = season_df[list(game_df.columns)]
        return season_df.add(game_df, fill_value=0)

    # combine dfs
    season_df = combine_dfs(season_df, game_df)

    # Adding additional metrics
    season_df["losses"] = season_df["games"] - season_df["wins"]

    # Avoid division by zero for record
    season_df["record"] = season_df.apply(
        lambda row: row["wins"] / row["games"] if row["games"] > 0 else 0.0,
        axis=1,
    )

    season_df["points/toss"] = season_df.apply(
        lambda row: float("inf")
        if row["tosses"] == 0
        else row["points"] / row["tosses"],
        axis=1,
    )
    season_df["catches/drop"] = season_df.apply(
        lambda row: float("inf")
        if row["drops"] == 0
        else row["catches"] / row["drops"],
        axis=1,
    )

    season_df["offensive rank"] = season_df["points/toss"].rank(
        ascending=False, method="min"
    )
    season_df["defensive rank"] = season_df["catches/drop"].rank(
        ascending=False, method="min"
    )

    # round all stats to three decimal places
    season_df = season_df.round(3)

    # Fill NaN values with 0 for integer columns before casting
    for col in season_df.columns:
        if col not in ["points/toss", "catches/drop", "record"]:
            season_df[col] = pd.to_numeric(season_df[col], errors="coerce").fillna(0).astype(int)

    print("\nStats saved\n")

    # save file
    season_df.to_csv("snappa_tourney.csv")
