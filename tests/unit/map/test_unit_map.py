"""
Unit tests for the Map class
"""

import pytest

from map.map import Map

@pytest.fixture
def map(tmp_path):
    map = (
        "#######\n"
        "#^# # #\n"
        "# ### #\n"
        "#     #\n"
        "#####E#\n"
    )
    start = (1, 1)
    size = (5, 7)
    dir = tmp_path / "maps"
    dir.mkdir()
    file = dir / "map.txt"
    file.write_text(map)
    return file, start, size


def test_init_map(map):
    path, start, size = map
    map = Map(path)

    assert map.start_position() == start
    assert map._size == size

def test_getitem_setitem(map):
    path, _, _ = map
    map = Map(path)

    assert map[(0, 0)] == "#"
    map[(0, 0)] = "X"
    assert map[(0, 0)] == "X"
