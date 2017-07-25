
class CalculationConditions:
    """Implementation of a class to hold the conditions of the calculation."""

    def __init__(self, pi_algorithm, approximation_algorithm, precision):
        self.__pi_algorithm = pi_algorithm
        self.__approximation_algorithm = approximation_algorithm
        self.__precision = precision

    def get_pi_algorithm(self):
        return self.__pi_algorithm

    def get_approximation_algorithm(self):
        return self.__approximation_algorithm

    def get_precision(self):
        return self.__precision