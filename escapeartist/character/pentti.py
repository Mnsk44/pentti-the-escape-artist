"""
Class representing a movable character in the maze.
"""

from typing import Tuple

from util.constants import DOWN, LEFT, RIGHT, UP


class Pentti:
    """
    Pentti knows his location and can move to any available adjacent space.
    """

    def __init__(self, row: int, col: int) -> None:
        self._pos = {
            "row": row,
            "col": col,
        }
        self._orientation = UP

    def position(self) -> Tuple[int, int]:
        return (self._pos["row"], self._pos["col"])

    def orientation(self) -> str:
        return self._orientation

    @property
    def left(self) -> Tuple[int, int]:
        return (self._pos["row"], self._pos["col"] - 1)

    @property
    def right(self) -> Tuple[int, int]:
        return (self._pos["row"], self._pos["col"] + 1)

    @property
    def up(self) -> Tuple[int, int]:
        return (self._pos["row"] - 1, self._pos["col"])

    @property
    def down(self) -> Tuple[int, int]:
        return (self._pos["row"] + 1, self._pos["col"])

    def move_up(self) -> None:
        self._pos.update({"row": self._pos["row"] - 1})
        self._orientation = UP

    def move_right(self) -> None:
        self._pos.update({"col": self._pos["col"] + 1})
        self._orientation = RIGHT

    def move_down(self) -> None:
        self._pos.update({"row": self._pos["row"] + 1})
        self._orientation = DOWN

    def move_left(self) -> None:
        self._pos.update({"col": self._pos["col"] - 1})
        self._orientation = LEFT
