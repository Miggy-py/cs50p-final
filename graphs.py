import plotly.express as px
from player_util import start_player_csv
from player import Player
from stats import get_player_stats


def main():
    my_player : Player = Player("Lebron James")
    career = get_player_stats(my_player)
    print(career)

    career["YEAR"] = career["SEASON_ID"].str[:4].astype(int)
    fig = px.line(career, x="YEAR", y="PTS", markers=True, title="LeBron PTS by Year")
    fig.update_layout(xaxis=dict(tickmode="linear", dtick=1))

    fig.show()


if __name__ == "__main__":
    main()