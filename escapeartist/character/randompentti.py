"""
'Algorithm' that forces Pentti to randomly walk in the maze until exit is found
"""

import random
from typing import Callable, List

from character.pentti import Pentti
from map.map import Map
from util.constants import BLOCK, EXIT, VISITED, PENTTI


class RandomPentti(Pentti):
    """
    Pentti doesn't have the map and will randomly walk in the maze, trying to
    find an exit.
    """

    def __init__(self, map: Map) -> None:
        super().__init__(*map.start_position())
        self._map = map
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

    def possible_moves(self) -> List[Callable]:
        moves = []
        if self._can_move_left():
            moves.append(self.move_left)
        if self._can_move_right():
            moves.append(self.move_right)
        if self._can_move_up():
            moves.append(self.move_up)
        if self._can_move_down():
            moves.append(self.move_down)
        return moves

    def _can_move_left(self) -> bool:
        row, col = self.position()
        return self._map.is_available_position(row, col-1)

    def _can_move_right(self) -> bool:
        row, col = self.position()
        return self._map.is_available_position(row, col+1)

    def _can_move_up(self) -> bool:
        row, col = self.position()
        return self._map.is_available_position(row-1, col)

    def _can_move_down(self) -> bool:
        row, col = self.position()
        return self._map.is_available_position(row+1, col)