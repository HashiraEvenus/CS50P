from numb3rs import validate

def test_first():
    assert validate("125.500.500.500") == False

def test_len():
    assert validate("125.5.5.5.5") == False