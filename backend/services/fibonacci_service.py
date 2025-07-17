from typing import List

from utils.logger import logger


class FibonacciService:
    @staticmethod
    def get_fibonacci(n: int) -> List[int]:
        if n == 1:
            sequence = [0]
            logger.info(f"Calculated Fibonacci sequence for {n}: {sequence}")
            return sequence
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[-1] + sequence[-2])
        logger.info(
            f"Calculated Fibonacci sequence for {n} numbers: {sequence}"
        )
        return sequence
