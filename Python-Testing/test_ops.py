from ops import add, divide
import pytest

def test_add():
    assert add(5,2) == 7, "5 + 2 should be 7"
    assert add(-1,2) == 1, "-1 + 2 should be 1"
    assert add(5,0) == 5, "5 + 0 should be 5"

def test_divide():
    with pytest.raises(ValueError, match="can't divide with 0"):
        divide(10, 0)

