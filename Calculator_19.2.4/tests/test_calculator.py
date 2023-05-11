import pytest
from app.calc import Calculator


class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_adding_succsess(self):
        assert self.calc.adding(self, 5, 5) == 10

    def test_subtraction_succsess(self):
        assert self.calc.subtraction(self, 5, 5) == 0

    def test_division_succsess(self):
        assert self.calc.division(self, 5, 5) == 1

    def test_multiply_succsess(self):
        assert self.calc.multiply(self, 5, 5) == 25