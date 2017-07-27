import unittest
from mpmath import *
import _src_path
from overlap_calculator.alpha_calculator.algorithm_runner import AlgorithmRunner
from overlap_calculator.alpha_calculator.algorithm_runner import AlgorithmType as AlphaAlgorithmType
from utils.pi.pi_util import PiUtility
from utils.pi.pi_util import AlgorithmType as PiAlgorithmType


# for precision in range(1 , 40):
#     alpha = AlgorithmRunner.calculate_alpha(AlgorithmType.Newton, precision)
#     print(precision, "-iter alpha is:  ", nstr(alpha, precision + 1))


class TestAlphaCalculation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        PiUtility.init_pi(PiAlgorithmType.BBP, 12)

    def test_alpha_10dp_accuracy(self):
        """Checking the accuracy of the calculation : 10 dp."""
        print("Test of alpha calculation with 10 decimal precision")
        alpha = AlgorithmRunner.calculate_alpha(AlphaAlgorithmType.Newton, 10)
        self.assertTrue(almosteq(alpha, mpmathify("2.3098814600", strings=True), 1e-10))
        print("=======================")

    def test_alpha_10dp_precision(self):
        """Checking if the results repeat under the same conditions."""
        print("Test of alpha calculation with 10 decimal precision [repeat]")
        alpha = AlgorithmRunner.calculate_alpha(AlphaAlgorithmType.Newton, 10)
        self.assertTrue(almosteq(alpha, mpmathify("2.3098814600", strings=True), 1e-10))
        print("=======================")

    def test_alpha_1dp_precision(self):
        """Checking the accuracy of the calculation : 1 dp."""
        print("Test of alpha calculation with 1 dp")
        alpha = AlgorithmRunner.calculate_alpha(AlphaAlgorithmType.Newton, 1)
        self.assertTrue(almosteq(alpha, mpmathify("2.3098814600", strings=True), 1e-1))
        print("=======================")

    def test_alpha_5dp_precision(self):
        """Checking the accuracy of the calculation : 5 dp."""
        print("Test of alpha calculation with 5 dp")
        alpha = AlgorithmRunner.calculate_alpha(AlphaAlgorithmType.Newton, 5)
        self.assertTrue(almosteq(alpha, mpmathify("2.3098814600", strings=True), 1e-5))
        print("=======================")

    def test_alpha_20dp_precision(self):
        """Checking the accuracy of the calculation : 20 dp."""
        print("Test of alpha calculation with 20 dp")
        PiUtility.init_pi(PiAlgorithmType.BBP, 22)
        alpha = AlgorithmRunner.calculate_alpha(AlphaAlgorithmType.Newton, 20)
        self.assertTrue(almosteq(alpha, mpmathify("2.3098814600100572608867", strings=True), 1e-20))
        print("=======================")


if __name__ == '__main__':
    unittest.main()