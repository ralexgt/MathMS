from utils.logger import logger


class FactorialService():
    @staticmethod
    def get_factorial(num: int) -> int:
        result = 1
        for i in range(1, num + 1):
            result *= i
        logger.info(f"Calculated factorial for {num}: {result}")
        return result
