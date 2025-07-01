import requests
from player import Player
from nba_api.stats.endpoints import playercareerstats


def get_player_stats(player: Player):
    career = playercareerstats.PlayerCareerStats(player_id=player.id)

    return career.get_data_frames()[0]
