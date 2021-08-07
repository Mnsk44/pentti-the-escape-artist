"""
Class representing a movable character in the maze.
"""


from typing import Tuple


class Pentti:
    """
    Pentti knows his location and can move to any available adjacent space.
    """

    def __init__(self, coord_x: int, coord_y: int) -> None:
        self._pos = {
            "x": coord_x, 
            "y": coord_y,
        }

    def position(self) -> Tuple[int, int]:
        return (self._pos["x"], self._pos["y"])

    def move_left(self) -> None:
        self._pos.update({"x": self._pos["x"] - 1})
    
    def move_up(self) -> None:
        self._pos.update({"y": self._pos["y"] + 1})
    
    def move_right(self) -> None:
        self._pos.update({"x": self._pos["x"] + 1})
    
    def move_down(self) -> None:
        self._pos.update({"y": self._pos["y"] - 1})
