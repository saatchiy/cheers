from mpmath import nstr
from enum import Enum
from .pi_algorithms.gregory_leibniz import GregoryLeibniz
from .pi_algorithms.bbp import BBP
from exceptions.calculation_exception import CalculationException

# This is a static util class that provides a function for
# calculating the PI number

ALGORITHMS = {
    0: BBP,
}

class AlgorithmType(Enum):
    BBP = 0
    GregoryLeibniz = 1


class PiUtility:

    __DEFAULT_PRECISION = 3
    __precision = ''
    __pi = 0
    __algorithm = AlgorithmType.BBP

    @classmethod
    def init_pi(cls, algorithm_type, precision = __DEFAULT_PRECISION):
        """Starts the calculation of PI number.

        Args:
            algorithm_type: The algorithm to be used for the calculation
            which is one of the enum items of AlgorithmType
            precision: The desired precision of the calculation (default 3)

        Returns:
            A mp float number calculation of PI.
        """

        cls.__precision = precision
        cls.__algorithm = algorithm_type
        
        try:
            cls.__calculate_pi()
        except CalculationException as err:
            raise err


    @classmethod
    def pi(cls):
        return cls.__pi

    @classmethod
    def __calculate_pi(cls):
        """Internal function for calculation of pi. This function calls
        the appropriate algorithm implementation based on the selection of
        the user.

        Args:
            algorithm_type: The algorithm to be used for the calculation

        Returns:
            A decimal number calculation of PI.
        """
        
        try:
            print("\nCalculation of PI constant started.")
            cls.__pi = ALGORITHMS[cls.__algorithm.value].calculate(cls.__precision)
            print("PI with the precision of", cls.__precision, "is:", nstr(cls.__pi, cls.__precision))
        except KeyError:
            cls.__pi = 0
            raise CalculationException("No implementation exists for the selected pi calculation algorithm.")
        

    @classmethod
    def get_algorithm(cls):
        return cls.__algorithm
