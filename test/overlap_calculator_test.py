import unittest
from mpmath import *
import _src_path
from overlap_calculator.overlap_calculator import OverlapCalculator
from overlap_calculator.calculation_conditions import CalculationConditions
from overlap_calculator.alpha_calculator.algorithm_runner import AlgorithmType as AlphaAlgorithmType
from utils.pi.pi_util import PiUtility
from utils.pi.pi_util import AlgorithmType as PiAlgorithmType

# length = OverlapCalculator.calculate_overlapping_length(20)
# print("Overlapping length :", nstr(length, 15))

# length = OverlapCalculator.calculate_overlapping_length(20000000000)
# print("Overlapping length :", nstr(length, 15))

# length = OverlapCalculator.calculate_overlapping_length(mpf(0.0003))
# print("Overlapping length :", nstr(length, 15))

class TestOverlapCalculation(unittest.TestCase):

    def test_length_10dp_r1_accuracy(self):
        """Checking the accuracy of the calculation : 10 dp."""
        print("Test for coaster radius = 1")
        conditions = CalculationConditions(PiAlgorithmType.BBP, AlphaAlgorithmType.Newton, 10)
        radius = 1
        result = OverlapCalculator.calculate_overlapping_length(radius, conditions)
        self.assertTrue(almosteq(result.get_overlapping_length(), mpmathify("1.1920544934", strings=True), 1e-10))
        print("=======================")

    def test_length_10dp_r1_precision(self):
        """Checking if the results repeat under the same conditions."""
        print("Test for coaster radius = 1")
        conditions = CalculationConditions(PiAlgorithmType.BBP, AlphaAlgorithmType.Newton, 10)
        radius = 1
        result = OverlapCalculator.calculate_overlapping_length(radius, conditions)
        self.assertTrue(almosteq(result.get_overlapping_length(), mpmathify("1.1920544934", strings=True), 1e-10))
        print("=======================")

    def test_length_10dp_r0_accuracy(self):
        """Test for coaster radius = 0."""
        print("Test for coaster radius = 0")
        conditions = CalculationConditions(PiAlgorithmType.BBP, AlphaAlgorithmType.Newton, 10)
        radius = 0
        result = OverlapCalculator.calculate_overlapping_length(radius, conditions)
        self.assertTrue(almosteq(result.get_overlapping_length(), mpmathify("0", strings=True), 1e-10))
        print("=======================")

    def test_length_10dp_r10000_accuracy(self):
        """Test for coaster radius = 10000."""
        print("Test for coaster radius = 10000")
        conditions = CalculationConditions(PiAlgorithmType.BBP, AlphaAlgorithmType.Newton, 10)
        radius = 10000
        result = OverlapCalculator.calculate_overlapping_length(radius, conditions)
        self.assertTrue(almosteq(result.get_overlapping_length(), mpmathify("11920.544934", strings=True), 1e-10))
        print("=======================")

    def test_length_10dp_r1000_000_accuracy(self):
        """Test for coaster radius = 1,000,000."""
        print("Test for coaster radius = 1,000,000")
        conditions = CalculationConditions(PiAlgorithmType.BBP, AlphaAlgorithmType.Newton, 10)
        radius = 1000000
        result = OverlapCalculator.calculate_overlapping_length(radius, conditions)
        self.assertTrue(almosteq(result.get_overlapping_length(), mpmathify("1192054.49341826", strings=True), 1e-10))
        print("=======================")

    def test_length_14dp_r0_0019_accuracy(self):
        """Test for coaster radius = 0.0019 with the precision of 14 ."""
        print("Test for coaster radius = 0.0019 with the precision of 14")
        conditions = CalculationConditions(PiAlgorithmType.BBP, AlphaAlgorithmType.Newton, 14)
        radius = mpmathify("0.0019", strings=True)
        result = OverlapCalculator.calculate_overlapping_length(radius, conditions)
        self.assertTrue(almosteq(result.get_overlapping_length(), mpmathify("0.00226490353746183460458808", strings=True), 1e-14))
        print("=======================")

    def test_length_20dp_r0_000019_accuracy(self):
        """Test for coaster radius = 0.000019 with the precision of 20 ."""
        print("Test for coaster radius = 0.000019 with the precision of 20")
        conditions = CalculationConditions(PiAlgorithmType.BBP, AlphaAlgorithmType.Newton, 20)
        radius = mpmathify("0.000019", strings=True)
        result = OverlapCalculator.calculate_overlapping_length(radius, conditions)
        self.assertTrue(almosteq(result.get_overlapping_length(), mpmathify("0.0000226490353746183460458808", strings=True), 1e-20))
        print("=======================")

if __name__ == '__main__':
    unittest.main()