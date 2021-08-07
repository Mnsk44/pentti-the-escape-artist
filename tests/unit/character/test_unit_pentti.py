"""
Unit tests for character/pentti
"""

from escapeartist.character.pentti import Pentti

def test_init_pentti():
    pentti = Pentti(0, 10)

    assert pentti.position() == (0, 10)
