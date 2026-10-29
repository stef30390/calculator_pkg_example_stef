import pytest

from calculator_pkg_example_stef.calculator import Calculator

class TestCalculator:
    def test_add (self) -> None:
        assert Calculator().add(1,2) == 3, "Add failed!"

    def test_subtract (self) -> None:
        assert Calculator().substract(5,3) == 2, "Subtract failed!"

    def test_multiply (self) -> None:
        assert Calculator().multiply(2,3) == 6, "Multiply failed!"  

    def test_divide (self) -> None:
        assert Calculator().divide(6,2) == 3, "Divide failed!"

    def test_divide_zero(self) -> None:
        with pytest.raises(ZeroDivisionError):
            Calculator().divide(1,0)