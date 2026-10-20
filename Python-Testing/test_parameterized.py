import pytest
from parameterized import is_prime

@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True)
])
def test_is_prime(num, expected):
    assert is_prime(num) == expected