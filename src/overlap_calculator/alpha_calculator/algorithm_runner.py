from .approximation_algorithms.newton import Newton
from enum import Enum

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
        return cls.__execute(algorithm_type, precision)


    @classmethod
    def __execute(cls, algorithm_type, precision):
        """Internal function for execution of the selected algorithm. 

        Args:
            algorithm_type: One of AlgorithmType enum.

        Returns:
            The result of the execution of the specified algorithm.
        """
        print("Calculation of alpha angle started.")
        return ALGORITHMS[algorithm_type.value].calculate(precision)
