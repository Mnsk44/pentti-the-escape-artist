"""
Unit tests for character/pentti
"""

from escapeartist.character.pentti import Pentti


def test_init_pentti():
    pentti = Pentti(0, 10)

    assert pentti.position() == (0, 10)

def test_move_up():
    pentti = Pentti(10, 10)

    pentti.move_up()
    assert pentti.position() == (9, 10)

def test_move_right():
    pentti = Pentti(10, 10)

    pentti.move_right()
    assert pentti.position() == (10, 11)

def test_move_down():
    pentti = Pentti(10, 10)

    pentti.move_down()
    assert pentti.position() == (11, 10)

def test_move_left():
    pentti = Pentti(10, 10)

    pentti.move_left()
    assert pentti.position() == (10, 9)