from working import convert
import pytest

def test_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
def test_vr():
    with pytest.raises(ValueError):
        convert("9:61 AM to 5:67 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")