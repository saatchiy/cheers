from enum import Enum
from mpmath import nstr
from .approximation_algorithms.newton import Newton
from exceptions.calculation_exception import CalculationException

# This is a module that provides an implementation for calculating 
# the approximation of Alpha

# This dictionary holds the classes of implemented algorithms
ALGORITHMS = {
    0: Newton,
}

# This is an enum for different approximation algorithms
# which are used for the calculation of alpha
class AlgorithmType(Enum):
    Newton = 0
    Bisection = 1


class AlgorithmRunner:

    __DEFAULT_PRECISION = 5

    @classmethod
    def calculate_alpha(cls, algorithm_type, precision = __DEFAULT_PRECISION):
        """Starts the calculation of Alpha.

        Args:
            algorithm_type: One of AlgorithmType enum. The algorithm to be used
                for the calculation which is one of the enum items of AlgorithmType
            precision: The desired precision of the calculation (default 5)

        Returns:
            The result of the execution of the specified algorithm.
        """

        try:
            return cls.__execute(algorithm_type, precision)
        except CalculationException as err:
            raise err


    @classmethod
    def __execute(cls, algorithm_type, precision):
        """Internal function for execution of the selected algorithm. 

        Args:
            algorithm_type: One of AlgorithmType enum.

        Returns:
            The result of the execution of the specified algorithm.
        """
        print("\nCalculation of alpha angle started.")
        try:
            alpha = ALGORITHMS[algorithm_type.value].calculate(precision)
            print("Alpha calculated to {} decimal precision as {}".format(precision, nstr(alpha, precision + 1)))
            return alpha
        except KeyError:
            raise CalculationException("No implementation exists for the selected alpha approximation algorithm.")
