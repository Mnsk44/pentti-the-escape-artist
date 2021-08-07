"""
Shared fixtures for unit testing the project
"""

import pytest

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