""" Home task calculator module """
from math import sqrt

class Calculator:

    def int_validation(self, x: int, y: int):
        """Checker for int value"""
        return not isinstance(x, int) or not isinstance(y, int)

    """ Calculator implementation """
    def add(self, x: int, y: int) -> int:
        """ Add to attributes to each other """
        if self.int_validation(x, y):
            raise TypeError
        return x + y

    def subtract(self, x: int, y: int) -> int:
        """ Subtract one attribute from another """
        if self.int_validation(x, y):
            raise TypeError
        return x - y

    def divide(self, x: int, y: int) -> float:
        """ Divide x attribute on y """
        if self.int_validation(x, y):
            raise TypeError
        return x / y

    def multiply(self, x: int, y: int) -> int:
        """ Multiply x attribute on y """
        if self.int_validation(x, y):
            raise TypeError
        return x * y

    def mod(self, x: int, y: int) -> int:
        """ Take mod of one attribute from another """
        if self.int_validation(x, y):
            raise TypeError
        return x % y

    def power(self, x: int, y: int) -> int:
        """ Raise attributes x to a power y """
        if self.int_validation(x, y):
            raise TypeError
        return x ** y

    def root(self, x: int) -> float:
        """ Take a root from attributes """
        if not isinstance(x, int):
            raise TypeError
        if x < 0:
            raise ValueError
        return sqrt(x)