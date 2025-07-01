from player_util import start_player_csv
from player import Player
from stats import get_player_stats
from graphs import compare_players_over_time
from nba_api.stats.endpoints import playercareerstats
from typing import List


def main():
    start_player_csv()

    start_program()


def start_program() -> None:
    stat_types = playercareerstats.PlayerCareerStats.expected_data.get("CareerTotalsAllStarSeason")
    player_list: List[str] = []

    print("Compare NBA Player Stats")
    print("Up to 5")

    while len(player_list) <= 5:
        player = input("Player (Exit w/ 'E'): ".strip())

        if player == "E":
            break
                    
        player_list.append(player)

    while True:
        stat = input("Compare by ('H' for help): ".strip())

        if stat == "H":
            print(stat_types)
            continue

        if stat not in stat_types:
            print("Invalid stat type")

        break

    compare_players_over_time(player_list, stat)


if __name__ == "__main__":
    main()
