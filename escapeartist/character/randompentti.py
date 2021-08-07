"""
'Algorithm' that forces Pentti to randomly walk in the maze until exit is found
"""

import random
from typing import List

from character.trackerpentti import TrackerPentti
from map.map import Map
from util.constants import EXIT, VISITED, PENTTI


class RandomPentti(TrackerPentti):
    """
    Pentti doesn't have the map and will randomly walk in the maze, trying to
    find an exit.
    """

    def __init__(self, map: Map) -> None:
        super().__init__(map)
        self._history: List[Map] = [map]

    def random_escape(self, limit = 10000) -> None:
        for round in range(limit):
            if self._map[self.position()] == EXIT:
                print(f"Pentti escaped in {round} steps")
                print(self._map)
                return
            self._history.append(self._map)

            movements = self.possible_moves()
            self._map[self.position()] = VISITED

            random.choice(movements)()
            self._map[self.position()] = PENTTI
        print(f"Pentti was exhausted after {limit} steps, Pentti did not escape...")
        print(self._map)