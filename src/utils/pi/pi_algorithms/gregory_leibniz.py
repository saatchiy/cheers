from mpmath import mpf
import math
from utils.algorithm_base import AlgorithmBase

class GregoryLeibniz(AlgorithmBase):
    """Implementation of Pi using Gregory-Leibniz algorithm."""
    @staticmethod
    def calculate(precision):
        """Calculates Pi number.

        Args:
            precision: The desired precision of the calculation

        Returns:
            A decimal number calculation of PI.
        """
        mp.dps = 30
        
        # For the first iteration value of one should be passed as a divisor
        divisor = GregoryLeibniz.__recurse(1, precision)

        print("divisor is: ", divisor)

        calculated_pi = mpf(4) / mpf(divisor)

        print("Calculation finished.")
        print("PI value is: ", calculated_pi)

    @staticmethod
    def __recurse(divisor, iter_count):
        """Recursive function which does the calculation.

        Args:
            iter_count: The counter to keep track of the recursion
            divisor: The divisor part of the algorithm
        """
        divisor = mpf(math.pow((iter_count * 2) + 1, 2)) / mpf(divisor)
        print("after power: ", divisor)
        if iter_count == 0:
            divisor += 1
            print("after addition: ", divisor)
            return divisor
        else:
            divisor += 2
            print("divisor is: ", divisor)
            return GregoryLeibniz.__recurse(divisor, iter_count - 1)
