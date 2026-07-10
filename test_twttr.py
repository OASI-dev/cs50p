from twttr import shorten


def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("CS50") == "CS50"