"""Practice the pytest .."""
import pytest

class clac:
        
        def add(n1,n2):
            return n1+n2
        def sub(n1,n2):
            return n1-n2
        def multi(n1,n2):
            return n1*n2
        def divi(n1,n2):
            return n1/n2

@pytest.fixture
def class_instance():
      return clac()
def test_add(class_instance):
      assert class_instance.add(2,4) ==6

def test_multi(class_instance):
    result = class_instance.multi(2,4)
    assert result == 8







