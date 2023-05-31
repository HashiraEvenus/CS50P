from plates import is_valid

def test_fail_length():
    assert is_valid("AAA2222") == False
def test_number():
    assert is_valid("A2") == False
def test_fail_0():
    assert is_valid("AA01") == False
def test_fail_number():
    assert is_valid("AAA22A")==False
def test_punc():
    assert is_valid("EA2 ,")==False