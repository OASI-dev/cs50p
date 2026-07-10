from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/4") == (1, 4)
    assert convert("3/4") == (3, 4)
    assert convert("1/1") == (1, 1)


def test_convert_types():
    x, y = convert("3/4")
    assert isinstance(x, int)
    assert isinstance(y, int)


def test_convert_error():
    with pytest.raises(ValueError):
        convert("5/4")


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"