from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO there") == 0


def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("howdy") == 20


def test_other():
    assert value("bonjour") == 100
    assert value("goodbye") == 100