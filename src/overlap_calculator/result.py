import CalculationConditions

class Result:
    """Implementation of a class to hold a result and conditions of the calculation."""

    def __init__(self, radius, conditions, length, alpha, pi):
        self.__coaster_radius = radius
        self.__calculation_conditions = conditions
        self.__overlapping_length = length
        self.__alpha = alpha
        self.__pi = pi

    def get_coaster_radius(self):
        return self.__coaster_radius

    def get_pi_algorithm(self):
        return self.__calculation_conditions.get_pi_algorithm()

    def get_approximation_algorithm(self):
        return self.__calculation_conditions.get_approximation_algorithm()

    def get_precision(self):
        return self.__calculation_conditions.get_precision()

    def get_overlapping_length(self):
        return self.__overlapping_length

    def get_alpha(self):
        return self.__alpha

    def get_pi(self):
        return self.__pi
