from player_util import start_player_csv
from player import Player
from stats import get_player_stats


def main():
    start_player_csv()

    my_player : Player = Player("Lebron James")

    career = get_player_stats(my_player)

    print(career)



if __name__ == "__main__":
    main()
