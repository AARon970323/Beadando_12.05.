import pytest
from calculator.calculator import Calculator

def test_add():
    c = Calculator()
    assert c.add(1, 2) == 3

def test_sub():
    c = Calculator()
    assert c.sub(5, 2) == 3

def test_mul():
    c = Calculator()
    assert c.mul(3, 3) == 9

def test_div():
    c = Calculator()
    assert c.div(6, 2) == 3

def test_div_error():
    c = Calculator()
    import pytest
    with pytest.raises(ZeroDivisionError):
        c.div(1, 0)

