"""
The Most advanced Pentti there is! He has the map and will do a Breadth First Search
to find the shorthest route before moving towards the finish!
"""
from copy import deepcopy
from collections import Counter
from queue import Queue
from typing import List, Tuple

from character.trackerpentti import TrackerPentti
from character.usablepentti import UsablePentti
from map.map import Map
from util.constants import VISITED

class BFSPentti(UsablePentti):
    """
    Pentti has a map of the maze and will find the optimal route before starting
    his journey!

    Due to the multidirectional nature of BFS, this class deviates from the single-direction
    Pentti -implementations as it needs to track multiple possible routes at the same time.
    """

    def __init__(self, map: Map) -> None:
        self._map: Map = map
        self._history: List[Map] = []

    def escape_maze(self, limit: int = 10000):
        self._bfs_escape()
        print(self._map)
        print(f"Pentti escaped in {self._count_path_length()} steps! Limit was {limit}")
        print(f"Search checked {len(self._history)} positions!")


    def _bfs_escape(self) -> None:
        """
        BFS Search with a queue. A new Pentti is sent to each direction, keeping
        track of his own movements, and marking the positions he visited into the
        common map.
        """
        queue: Queue = Queue()
        queue.put(TrackerPentti(deepcopy(self._map)))

        while queue:
            pentti: TrackerPentti = queue.get()

            if self._is_visited(pentti.position()):
                # Skip if queued move was completed by earlier queue object
                continue

            if pentti._win_condition():
                return self._update_win(pentti)

            self._document_movements(pentti)

            for adjacent in [pentti.left, pentti.right, pentti.up, pentti.down]:
                if self._is_unvisited_and_available(adjacent):
                    pentti._map.start_position = adjacent
                    queue.put(TrackerPentti(deepcopy(pentti._map)))

    def _is_visited(self, coords: Tuple[int, int]):
        return self._map[coords] == VISITED

    def _mark_visited(self, coords: Tuple[int, int]):
        self._map[coords] = VISITED

    def _is_unvisited_and_available(self, coords: Tuple[int, int]):
        return self._map.is_available_position(*coords) and not self._is_visited(coords)

    def _update_win(self, pentti: TrackerPentti):
        pentti._mark_winning_position()
        self._map = pentti._map

    def _document_movements(self, pentti: TrackerPentti):
        self._history.append(deepcopy(self._map))
        self._mark_visited(pentti.position())
        pentti._mark_visited()

    def _count_path_length(self) -> int:
        return Counter(str(self._map))["+"] + 1