import pytest
import sys

def myfunc(data):
    if type(data) not in [int, list, tuple]:
        raise TypeError("должно быть int, list, tuple")
    return type(data)


def test_type_mismatch():
    with pytest.raises(TypeError):
        myfunc(42.2)

def test_str0():
    assert myfunc(4) == int, 'Тип данных не int, list, tuple'

def test_str1():
    assert myfunc(0) == int, 'Тип данных не int, list, tuple'

def test_float1():
    assert myfunc((22.2, 432)) == tuple, 'Тип данных не int, list, tuple'

def test_float2():
    assert myfunc([5, 45, 5.5]) == list, 'Тип данных не int, list, tuple'

data = [(-2147483648, int),(0, int), (2147483648 , int)]
@pytest.mark.parametrize("info, expected", data)
def test_myfunc(info, expected):
    assert myfunc(info)
