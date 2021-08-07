"""
Class representing a movable character in the maze.
"""


from typing import Tuple


class Pentti:
    """
    Pentti knows his location and can move to any available adjacent space.
    """

    def __init__(self, row: int, col: int) -> None:
        self._pos = {
            "row": row,
            "col": col,
        }

    def position(self) -> Tuple[int, int]:
        return (self._pos["row"], self._pos["col"])

    def move_up(self) -> None:
        self._pos.update({"row": self._pos["row"] - 1})

    def move_right(self) -> None:
        self._pos.update({"col": self._pos["col"] + 1})

    def move_down(self) -> None:
        self._pos.update({"row": self._pos["row"] + 1})

    def move_left(self) -> None:
        self._pos.update({"col": self._pos["col"] - 1})
