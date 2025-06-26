import pandas
from player_util import PLAYERS_CSV
from typing import Tuple

class Player:
    def __init__(self, inputted_name: str):
        self.name, self.id = self._get_player_info(inputted_name.strip())


    @property
    def name(self):
        return self._name
    

    @property
    def id(self):
        return self._id
    

    @name.setter
    def name(self, name: str):
        self._name = name

    
    @id.setter
    def id(self, id: int):
        self._id = id


    def _get_player_info(self, inputted_name) -> tuple[str, int]:
        df = pandas.read_csv(PLAYERS_CSV)

        match = df[df["full_name"].str.lower() == inputted_name.lower()]

        name = self._get_player_name(match)
        id = self._get_player_id(match)

        return (name, id)


    def _get_player_id(self, match) -> int:
        if not match.empty:
            return int(match.iloc[0]["id"])
        
        raise ValueError(f"Player '{self.name}' not found in cached CSV.")
    

    def _get_player_name(self, match) -> str:
        if not match.empty:
            return str(match.iloc[0]["full_name"])
        
        raise ValueError(f"Player '{self.name}' not found in cached CSV.")
    

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}"
