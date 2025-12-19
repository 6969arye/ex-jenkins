import pytest
from calc import add, divide

def test_add():
    assert add(2, 3) == 5, "Expected add(2, 3) to be 5"

def test_divide():
    assert divide(10, 2) == 5, "Expected divide(10, 2) to be 5"

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
