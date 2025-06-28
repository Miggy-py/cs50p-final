import plotly.express as px
import pandas as pd
from player_util import start_player_csv
from player import Player
from stats import get_player_stats
from typing import List


def main():
    start_player_csv()
    """
    my_player : Player = Player("Lebron James")
    career = get_player_stats(my_player)
    print(career)

    career["YEAR"] = career["SEASON_ID"].str[:4].astype(int)
    fig = px.line(career, x="YEAR", y="PTS", markers=True, title="LeBron PTS by Year")
    fig.update_layout(xaxis=dict(tickmode="linear", dtick=1))

    fig.show()
    """

    compare_players_over_time(["LeBron James", "Anthony Davis", "Stephen Curry"], "PTS")

def compare_players_over_time(player_list: List[str], y_axis: str = "PTS") -> None:
    if len(player_list) < 1:
        return None

    players: List[Player] = []

    for name in player_list:
        players.append(Player(name))

    combined_df = get_combined_data_frames(players)

    combined_df["YEAR"] = combined_df["SEASON_ID"].str[:4].astype(int)

    fig = px.line(
        combined_df,
        x="YEAR",
        y=y_axis,
        color="PLAYER_NAME",  # differentiates lines
        markers=True,
        title=f"{y_axis} per Season: {' vs '.join(player_list)}"
    )

    fig.update_layout(
        xaxis=dict(tickmode="linear", dtick=1),
        yaxis_title="Total Points",
    )

    fig.show()


def get_combined_data_frames(players: List[Player]) -> pd.DataFrame:
    data_frames = []

    for player in players:
        try:
            df = get_player_stats(player)
            df["PLAYER_NAME"] = player.name
            data_frames.append(df)
        except ValueError as e:
            print(f"Skipping {player.name}: {e}")

    combined_df = pd.concat(data_frames, ignore_index=True)

    return combined_df
 


if __name__ == "__main__":
    main()
