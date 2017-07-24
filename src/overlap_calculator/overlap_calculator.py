from mpmath import *
from .alpha_calculator.algorithm_runner import AlgorithmRunner, AlgorithmType

class OverlapCalculator:

    __PRECISION = 15
    __ALPHA = AlgorithmRunner.calculate_alpha(AlgorithmType.Newton, __PRECISION)
    __ALPHA_OVER_TWO = __ALPHA / mpf(2)

    @classmethod
    def calculate_overlapping_length(cls, coaster_radius):
        """Calculates the length of the overlapping segment.

        It uses alpha calculator class to find the length of the overlapping
        segment so that the overlapping area would be half of the area of a coaster

        Args:
            coaster_radius: The radius of each coaster. A mp float.

        Returns:
            The length of the overlapping segment. It is a mp float.
        """
        print("Calculation of overlapping length started.")
        print("Alpha with the precision of", cls.__PRECISION, "is:", nstr(cls.__ALPHA, cls.__PRECISION + 1))

        # formula is : l = 2R(1 - cos(alpha/2))

        radius = mpf(coaster_radius)

        overlapping_length = mpf(2) * radius * (mpf(1) - cos(cls.__ALPHA_OVER_TWO))

        return overlapping_length


    @classmethod
    def get_alpha(cls):
        return cls.__ALPHA