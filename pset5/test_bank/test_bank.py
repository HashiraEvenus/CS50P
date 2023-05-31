from bank import value

def test_hello():
    assert value("hEllo re manga") == 0
def test_h():
    assert value("heIa SoU Re mAnga") == 20

def test_random():
    assert value("geia sOu re manga") == 100