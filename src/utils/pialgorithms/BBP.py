from decimal import Decimal as D
import math
from .PiAlgorithmBase import PiAlgorithmBase

class BBP(PiAlgorithmBase):
    """Implementation of Pi using Bailey–Borwein–Plouffe formula."""
    @staticmethod
    def calculate(precision):
        """Calculates Pi number.

        Keyword arguments:
        precision -- the desired precision of the calculation
        """

        calculated_pi = D(0)

        for iter_num in range(precision, -1, -1):
            eight_factor = 8 * iter_num
            base_sixteen_factor = D(1) / D(math.pow(16, iter_num))
            current_iter_value = -(D(1) / D(eight_factor + 6))
            current_iter_value -= D(1) / D(eight_factor + 5)
            current_iter_value -= D(2) / D(eight_factor + 4)
            current_iter_value += D(4) / D(eight_factor + 1)
            calculated_pi += base_sixteen_factor * current_iter_value

        return calculated_pi
