from .pialgorithms.GregoryLeibniz import GregoryLeibniz
from .pialgorithms.BBP import BBP
from enum import Enum

# This is a static util class that provides a function for
# calculating the PI number

ALGORITHMS = {
    0: GregoryLeibniz,
    1: BBP,
}

class AlgorithmType(Enum):
    GregoryLeibniz = 0
    BBP = 1


class PiUtility:

    __DEFAULT_PRECISION = 3
    __precision = ''
    __pi = 0

    @classmethod
    def pi(cls, algorithm_type, precision = __DEFAULT_PRECISION):
        """Starts the calculation of PI number.

        Keyword arguments:
        algorithm_type -- The algorithm to be used for the calculation
        which is one of the enum items of AlgorithmType
        precision -- The desired precision of the calculation (default 3)
        """
        if cls.__pi == 0 or cls.__precision != precision:
            cls.__precision = precision
            cls.__calculate_pi(algorithm_type)

        return cls.__pi

    @classmethod
    def __calculate_pi(cls, algorithm_type):
        """Internal function for calculation of pi. This function calls
        the appropriate algorithm implementation based on the selection of
        the user.

        algorithm_type -- The algorithm to be used for the calculation
        """
        print("Calculation of PI constant started.")
        cls.__pi = ALGORITHMS[algorithm_type.value].calculate(cls.__precision)
