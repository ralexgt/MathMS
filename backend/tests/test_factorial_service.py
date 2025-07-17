from services.factorial_service import FactorialService


class TestFactorialService:
    def test_factorial_zero(self):
        assert FactorialService.get_factorial(0) == 1

    def test_factorial_one(self):
        assert FactorialService.get_factorial(1) == 1

    def test_factorial_positive(self):
        assert FactorialService.get_factorial(5) == 120
