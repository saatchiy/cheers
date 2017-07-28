from mpmath import *
from utils.pi.pi_util import PiUtility
from .alpha_calculator.algorithm_runner import AlgorithmRunner, AlgorithmType
from .result import Result
from exceptions.calculation_exception import CalculationException

class OverlapCalculator:

    __precision = 0
    __approximation_algorithm = AlgorithmType.Newton
    __alpha = 0
    __alpha_over_two = 0

    @classmethod
    def calculate_overlapping_length(cls, coaster_radius, conditions):
        """Calculates the length of the overlapping segment.

        It uses alpha calculator class to find the length of the overlapping
        segment so that the overlapping area would be half of the area of a coaster

        Args:
            coaster_radius: The radius of each coaster. A mp float.
            conditions: The conditions of the calculation. A CalculationCondition object.

        Returns:
            The length of the overlapping segment in the form of a result object.
        """

        try:
            # We only recalculate alpha and Pi if the conditions has been changed
            if not cls.__constants_calculated(conditions):
                # We initialize the pi value before starting the calculations
                PiUtility.init_pi(conditions.get_pi_algorithm(), conditions.get_precision() + int(5))
                
                cls.__precision = conditions.get_precision()
                cls.__approximation_algorithm = conditions.get_approximation_algorithm()
                cls.__alpha = AlgorithmRunner.calculate_alpha(cls.__approximation_algorithm, cls.__precision)
                cls.__alpha_over_two = cls.__alpha / mpf(2)

                print("Alpha with the precision of", cls.__precision, "is:", nstr(cls.__alpha, cls.__precision + 1))
        except CalculationException as err:
            raise err

        # formula is : l = 2R(1 - cos(alpha/2))
        print("\nCalculation of overlapping length for the radius of {} started.".format(coaster_radius))
        radius = mpf(coaster_radius)

        overlapping_length = mpf(2) * radius * (mpf(1) - cos(cls.__alpha_over_two))

        print("\nOverlapping length calculated at {} decimal places as {}".format(cls.__precision, overlapping_length))

        result = Result(radius, conditions, overlapping_length, cls.__alpha, PiUtility.pi())

        return result


    @classmethod
    def __constants_calculated(cls, conditions):
        if (PiUtility.pi() == 0 or cls.__alpha == 0 or
            conditions.get_precision() != cls.__precision or
            conditions.get_approximation_algorithm() != cls.__approximation_algorithm or
            conditions.get_pi_algorithm() != PiUtility.get_algorithm()):

            return False

        return True    
