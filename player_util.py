import pandas
import os
from nba_api.stats.static import players


PLAYERS_CSV = "players.csv"


def start_player_csv() -> None:
    # Stores players into players.csv once
    if os.path.exists(PLAYERS_CSV):
        # print("CSV already exists")
        return

    player_list = players.get_players()

    data_frame = pandas.DataFrame(player_list)

    data_frame.to_csv(PLAYERS_CSV, index=False)
