from seasons import get_date
import pytest

def test_get_date():

        with pytest.raises(TypeError):
              get_date("2000/3/3")
        



