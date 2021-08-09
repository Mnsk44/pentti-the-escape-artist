"""
Subclass of Pentti, capable of checking his surroundings and remembering his
tracks through a Map.

Further algorithm solutions will determine whether Pentti can use the Map or create
it along the way. The basic assumption is that Pentti can only see his immediate
adjacent tiles.
"""

from copy import deepcopy
from typing import Callable, List

from character.pentti import Pentti
from map.map import Map
from util.constants import EXIT, PENTTI, VISITED, VICTORY


class TrackerPentti(Pentti):
    """
    TrackerPentti can check his surroundings and determine in which directions he
    can move into.
    """
    def __init__(self, map: Map) -> None:
        super().__init__(*map.start_position)
        self._map = map
        self._history: List[Map] = [map]

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

    def _mark_visited(self) -> None:
        self._map[self.position()] = VISITED

    def _mark_current_position(self) -> None:
        self._map[self.position()] = PENTTI

    def _mark_winning_position(self) -> None:
        self._map[self.position()] = VICTORY

    def _win_condition(self) -> bool:
        return self._map[self.position()] == EXIT

    def _solve_maze(self, move_rule: Callable, limit: int = 10000) -> None:
        for round in range(limit):
            self._history.append(deepcopy(self._map))
            self._mark_visited()

            move_rule()

            if self._win_condition():
                self._mark_winning_position()
                print(self._map)
                print(f"Pentti escaped in {round} steps")
                return
            self._mark_current_position()
        print(self._map)
        print(f"Pentti was exhausted after {limit} steps, Pentti did not escape...")
