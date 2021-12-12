import main as m
import pytest

def test_soma():
    assert m.soma(200,20)

def test_sub():
    assert m.sub(20,60)

def test_mult():
    assert m.mult(5,5)

def test_div():
    assert m.div(100, 2)

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        m.div(10,0)



