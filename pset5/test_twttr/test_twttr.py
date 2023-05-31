from twttr import shorten

def test_shorten():

    assert shorten("DAvi,d1") == "Dv,d1"
    #assert shorten("dav,id") == "dv,d"
