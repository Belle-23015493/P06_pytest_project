from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 43
        b = 12
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 516
        assert result == expected

    def test_divide_not_zero(self):
        # arrange
        a = 45
        b = 15
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 3
        assert result == expected

    def test_divide_zero(self):
        # arrange
        a = 45
        b = 0
        cal = Calculator()

        # act & assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a, b)