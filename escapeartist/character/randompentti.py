"""
'Algorithm' that forces Pentti to randomly walk in the maze until exit is found
"""

import random
from typing import List

from character.trackerpentti import TrackerPentti
from map.map import Map
from util.constants import EXIT, VICTORY, VISITED, PENTTI


class RandomPentti(TrackerPentti):
    """
    Pentti doesn't have the map and will randomly walk in the maze, trying to
    find an exit.
    """

    def __init__(self, map: Map) -> None:
        super().__init__(map)
        self._history: List[Map] = [map]

    def random_escape(self, limit = 10000) -> None:
        self._solve_maze(self._random_move, limit)

    def _random_move(self):
        movements = self.possible_moves()
        random.choice(movements)()