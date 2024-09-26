"""Practice the pytest .."""
import pytest
import calculator as m
class Testclac:
    def test_multi(self):
        result = m.multi(2,4)
        result == 8
    def test_sub(self):
        result = m.sub(4,2)
        result == 2
    def test_add(self):
        result = m.add(2,4)
        assert result == 6