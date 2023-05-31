from um import count

def test_words():
    assert count("helloum") == 0
def test_case():
    assert count("Um hello") == 1
def test_space():
    assert count("um,hello") == 1
#def_three_in_1():
    #assert count("Um, helloum, um") == 2