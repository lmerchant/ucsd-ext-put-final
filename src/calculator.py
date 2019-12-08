"""
Calculator.py

Calculates addition, subtraction, multiplication and division of two numbers
"""


def add(num1, num2):
    """ Adds two numbers
    >>> add(2,4)
    6
    """
    return num1 + num2


def sub(num1, num2):
    """
    Subtracts two numbers
    >>> sub(2,4)
    -2
    """
    return num1 - num2


def mul(num1, num2):
    """
    Multiplies two numbers
    >>> mul(2,4)
    8
    """
    return num1 * num2


def div(num1, num2):
    """
    Divides two numbers
    >>> div(4,2)
    2.0
    
    Raises zero division error
    >>> div(4,0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return num1 / num2
