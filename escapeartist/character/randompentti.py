"""
'Algorithm' that forces Pentti to randomly walk in the maze until exit is found
"""

import random
from typing import List

from character.trackerpentti import TrackerPentti
from character.usablepentti import UsablePentti
from map.map import Map


class RandomPentti(TrackerPentti, UsablePentti):
    """
    Pentti doesn't have the map and will randomly walk in the maze, trying to
    find an exit.
    """

    def __init__(self, map: Map) -> None:
        super().__init__(map)

    def escape_maze(self, limit: int = 10000):
        self._random_escape(limit)

    def _random_escape(self, limit = 10000) -> None:
        self._solve_maze(self._random_move, limit)

    def _random_move(self):
        movements = self.possible_moves()
        random.choice(movements)()