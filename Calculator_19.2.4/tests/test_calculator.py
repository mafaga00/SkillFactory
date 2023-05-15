import pytest
from app.calc import Calculator


class TestCalculator:
    def setup(self):
        self.calc = Calculator()

    def test_adding(self):
        assert self.calc.adding(5, 5) == 10

    def test_subtraction(self):
        assert self.calc.subtraction(5, 5) == 0

    def test_division(self):
        assert self.calc.division(5, 5) == 1

    def test_multiply(self):
        assert self.calc.multiply(5, 5) == 25
