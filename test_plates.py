from plates import is_valid


def test_length():
    assert is_valid("CS") == True
    assert is_valid("CS50P") == False
    assert is_valid("C") == False
    assert is_valid("CS50PYTHON") == False


def test_alphanumeric():
    assert is_valid("CS 50") == False
    assert is_valid("CS-50") == False
    assert is_valid("CS50") == True


def test_starts_with_letters():
    assert is_valid("50CS") == False
    assert is_valid("5CS0") == False
    assert is_valid("C5S0") == False


def test_numbers_at_end():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("C0S0") == False


def test_no_leading_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True