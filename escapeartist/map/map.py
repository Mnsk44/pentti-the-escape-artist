"""
Class representing the map of a maze
"""

from typing import List, Tuple

from util.constants import BLOCK, EXIT, SPACE, START


class Map:
    """
    Map stores information about the underlying maze and can represent that visually.

    All coordinates and sizes are represented as rows and columns in this order.

    Map is assumed to be rectangular.
    """

    def __init__(self, map_path: str) -> None:
        self._map = self._load_map(map_path)
        self._start_pos = self._find_starting_position()
        self._size = self._determine_size()

    def __str__(self) -> str:
        return "\n".join(["".join(map_row) for map_row in self._map])

    def __getitem__(self, key: Tuple[int, int]) -> str:
        row, col = key
        return self._map[row][col]

    def __setitem__(self, key: Tuple[int, int], value: str) -> None:
        row, col = key
        self._map[row][col] = value

    def _load_map(self, path: str) -> List[List[str]]:
        with open(path, "r") as map_file:
            return [list(line.rstrip()) for line in map_file.readlines()]

    def _find_starting_position(self) -> Tuple[int, int]:
        """
        Finds the first instance of 'START', assuming one cannot start in multiple
        positions at once.
        """
        return [
            (row_index, row.index(START))
            for row_index, row in enumerate(self._map)
            if START in row
        ][0]

    def _determine_size(self) -> Tuple[int, int]:
        return (len(self._map), len(self._map[0]))

    def start_position(self):
        return self._start_pos

    def is_available_position(self, row, col) -> bool:
        try:
            return self[(row, col)] != BLOCK
        except IndexError:
            return False
