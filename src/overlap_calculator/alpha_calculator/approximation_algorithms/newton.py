from mpmath import *
from utils.pi.pi_util import PiUtility, AlgorithmType
from utils.algorithm_base import AlgorithmBase

class Newton(AlgorithmBase):
    """Implementation of the approximation algorithm to calculate alpha."""

    # The initial value for the first iteration of the newton algorithm
    __INITIAL_VALUE = mpf("2.5")

    # Decimal places
    __precision = 0

    # Pi / 2
    __pi_over_two = 0

    @classmethod
    def get_initial_value(cls):
        return cls.__INITIAL_VALUE

    @classmethod
    def calculate(cls, precision):
        """Calculates alpha.

        Args:
            precision: the desired precision of the calculation

        Returns:
            The result of the calculation which is the approximation of alpha angle.
        """

        # We calculate pi/2 only once before starting the calculations
        cls.__pi_over_two = PiUtility.pi() / mpf(2)

        # Setting the decimal places
        mp.dps = precision + 1

        # Initial value for newton approximation algorithm
        alpha = cls.__INITIAL_VALUE

        calculated_decimal_places = 1
        # The formula is:
        # alpha_n+1 = alpha_n - [(alpha_n - sin(alpha_n) - (pi/2)) / (1 - cos(alpha_n))]
        for iter_num in range(0, precision):
            alpha = cls.__calculate_next_alpha(alpha)
            if iter_num >= 1:
                # The convergence is quadratic, hence the number of
                # iterations based on the specified precision can be checked as follows
                calculated_decimal_places += 3 * (2**(iter_num - 1))
                if calculated_decimal_places >= precision:
                    break

        return alpha


    @classmethod
    def __calculate_original_function(cls, alpha):
        result = alpha - sin(alpha) - cls.pi_pver_two
        return result


    @classmethod
    def __calculate_diff_function(cls, alpha):
        result = mpf(1) - cos(alpha)
        return result


    @classmethod
    def __calculate_next_alpha(cls, alpha):
        subtraction_part = cls.__calculate_original_function(alpha) / cls.__calculate_diff_function(alpha)
        return alpha - subtraction_part
