"""
Unit tests for TrackerPentti
"""

from character.trackerpentti import TrackerPentti
from map.map import Map

def test_possible_moves(map):
    """
    See tests/unit/conftest.py for the fixture and map orientation.
    """
    path, _, _ = map
    map = Map(path)

    # Original position has one opening, down
    pentti = TrackerPentti(map)
    assert pentti.possible_moves() == [pentti.move_down]

    # Position (3, 3) has openings to the left and right
    map._start_pos = (3, 3)

    pentti = TrackerPentti(map)
    moves = pentti.possible_moves()
    assert len(moves) == 2
    assert pentti.move_right in moves
    assert pentti.move_left in moves

def test_crossing_edge_not_allowed(map):
    path, _, _ = map
    map = Map(path)
    map._start_pos = (0, 0)

    # In position (0, 0) there is no available moves: up and left are out of bounds
    # and right and down are walls
    pentti = TrackerPentti(map)

    assert len(pentti.possible_moves()) == 0