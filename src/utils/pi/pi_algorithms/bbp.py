from mpmath import mp, mpf
import math
from utils.algorithm_base import AlgorithmBase

class BBP(AlgorithmBase):
    """Implementation of Pi using Bailey–Borwein–Plouffe formula."""
    @staticmethod
    def calculate(precision):
        """Calculates Pi number.

        Args:
            precision: the desired precision of the calculation
        
        Returns:
            A decimal number calculation of PI.
        """
        mp.dps = precision + 1

        calculated_pi = mpf(0)

        # The formula is : 
        # PI = sum of ((1/(16^k) * [(4/(8k + 1)) - (2/(8k + 4)) - (1/(8k + 5)) - (1/(8k + 6))])
        for iter_num in range(precision + 15, -1, -1):
            eight_factor = 8 * iter_num
            base_sixteen_factor = mpf(1) / mpf(math.pow(16, iter_num))
            current_iter_value = -(mpf(1) / mpf(eight_factor + 6))
            current_iter_value -= mpf(1) / mpf(eight_factor + 5)
            current_iter_value -= mpf(2) / mpf(eight_factor + 4)
            current_iter_value += mpf(4) / mpf(eight_factor + 1)
            calculated_pi += base_sixteen_factor * current_iter_value

        return calculated_pi
