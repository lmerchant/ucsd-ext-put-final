import pytest
from src.calculator import *


@pytest.mark.parametrize('num1, num2, expected', [(1, 2, 3), (3, 4, 7), (5, 6, 11)])
def test_addition(num1, num2, expected):
    real = add(num1, num2)
    assert real == expected
        
@pytest.mark.parametrize('num1, num2, expected', [(0, 1, -1), (3, 1, 2), (5, 5, 0)])
def test_subtraction(num1, num2, expected):
    real = sub(num1, num2)
    assert real == expected
   
@pytest.mark.parametrize('num1, num2, expected', [(0, 2, 0), (1, 2, 2), (2, 3, 6)])
def test_multiplication(num1, num2, expected):
    real = mul(num1, num2)
    assert real == expected
   
@pytest.mark.parametrize('num1, num2, expected', [(2, 1, 2.0), (4, -2, -2.0), (0, 4, 0)])
def test_division(num1, num2, expected):
    real = div(num1, num2)
    assert real == expected
    
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(4, 0)
        
    
    
