"""Practice the pytest .."""
import pytest
import calculator as m
def test_add():
    result = m.py(2,4)
    assert result == 6