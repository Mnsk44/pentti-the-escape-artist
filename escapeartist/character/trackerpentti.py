"""
Subclass of Pentti, capable of checking his surroundings and remembering his
tracks through a Map.

Further algorithm solutions will determine whether Pentti can use the Map or create
it along the way. The basic assumption is that Pentti can only see his immediate
adjacent tiles.
"""

from typing import Callable, List

from character.pentti import Pentti
from map.map import Map


class TrackerPentti(Pentti):
    """
    TrackerPentti can check his surroundings and determine in which directions he
    can move into.
    """
    def __init__(self, map: Map) -> None:
        super().__init__(*map.start_position())
        self._map = map

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