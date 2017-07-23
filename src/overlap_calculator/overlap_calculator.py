from mpmath import *
from .alpha_calculator.algorithm_runner import AlgorithmRunner, AlgorithmType

class OverlapCalculator:

    __PRECISION = 15
    __ALPHA = AlgorithmRunner.calculate_alpha(AlgorithmType.Newton, __PRECISION)
    __ALPHA_OVER_TWO = __ALPHA / mpf(2)

    @classmethod
    def calculate_overlapping_length(cls, coaster_radius):

        print("Calculation of overlapping length started.")
        print("Alpha with the precision of", cls.__PRECISION, "is:", nstr(cls.__ALPHA, cls.__PRECISION + 1))

        # formula is : l = 2R(1 - cos(alpha/2))

        radius = mpf(coaster_radius)

        overlapping_length = mpf(2) * radius * (mpf(1) - cos(cls.__ALPHA_OVER_TWO))

        return overlapping_length


    @classmethod
    def get_alpha(cls):
        return cls.__ALPHA