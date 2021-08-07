"""
Right Hand Rule algorithm for Pentti to solve the maze with
"""

from typing import List

from map.map import Map
from util.constants import (
    DOWN, EXIT, LEFT, PENTTI, RIGHT, UP, VICTORY, VISITED
)

from character.trackerpentti import TrackerPentti


class RightHandPentti(TrackerPentti):
    """
    This Pentti knows that by having your right (or left) hand constantly on a
    wall shoud eventually take you to an exit. Assuming there's no loops in the
    maze...
    """

    def __init__(self, map: Map) -> None:
        super().__init__(map)
        self._history: List[Map] = [map]

    def right_hand_escape(self, limit = 10000) -> None:
        for round in range(limit):
            self._history.append(self._map)
            self._map[self.position()] = VISITED

            self._move_by_right_hand_rule()

            if self._map[self.position()] == EXIT:
                self._map[self.position()] = VICTORY
                print(self._map)
                print(f"Pentti escaped in {round} steps")
                return
            self._map[self.position()] = PENTTI
        print(self._map)
        print(f"Pentti was exhausted after {limit} steps, Pentti did not escape...")

    def _move_by_right_hand_rule(self):
        priorities = self._move_priority()
        possible_moves = self.possible_moves()
        for priority in priorities:
            if priority in possible_moves:
                priority()
                break

    def _move_priority(self):
        """
        In order to follow the right hand rule, Pentti needs to keep his right hand
        in touching the wall. This can be achieved by moving only in one direction
        and prioritizing anything that'll keep his right hand in the wall.

        The priority will need to change based on Pentti's orientation.
        """
        priorities = {
            UP: [self.move_right, self.move_up, self.move_left, self.move_down],
            RIGHT: [self.move_down, self.move_right, self.move_up, self.move_left],
            LEFT: [self.move_up, self.move_left, self.move_down, self.move_right],
            DOWN: [self.move_left, self.move_down, self.move_right, self.move_up],
        }
        return priorities[self.orientation()]

