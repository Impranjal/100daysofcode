"""
Markers in pytest:
1- xfail
2- fixture

"""
import pytest
import rest_api_python as rs
import calculator as c
#Skip the test we can do using pytest.mark.skip

@pytest.mark.skip(reason="Not interested")
def test_add():
    assert c.add(2,4) ==8
 
@pytest.mark.xfail
def test_add_list():
    assert c.add([1],[2]) == 8
    raise Exception


