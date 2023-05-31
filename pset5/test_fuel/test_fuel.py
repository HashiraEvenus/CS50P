from fuel import convert,gauge
import pytest

def test_convert():
    assert convert("89/100") == 89
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
    with pytest.raises(ValueError):
        convert("4/3")


    #-assert convert(1/0) == ZeroDivisionError
def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"