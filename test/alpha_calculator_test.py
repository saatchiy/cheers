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

    def test_alpha_10dp_accuracy(self):
        """Checking the accuracy of the calculation : 10 dp."""
        print("Test of alpha calculation with 10 decimal precision")
        PiUtility.init_pi(PiAlgorithmType.BBP, 12)
        alpha = AlgorithmRunner.calculate_alpha(AlphaAlgorithmType.Newton, 10)
        self.assertTrue(almosteq(alpha, mpmathify("2.3098814600", strings=True), 1e-10))
        print("=======================")

    def test_alpha_10dp_precision(self):
        """Checking if the results repeat under the same conditions."""
        print("Test of alpha calculation with 10 decimal precision [repeat]")
        PiUtility.init_pi(PiAlgorithmType.BBP, 12)
        alpha = AlgorithmRunner.calculate_alpha(AlphaAlgorithmType.Newton, 10)
        self.assertTrue(almosteq(alpha, mpmathify("2.3098814600", strings=True), 1e-10))
        print("=======================")

    def test_alpha_1dp_precision(self):
        """Checking the accuracy of the calculation : 1 dp."""
        print("Test of alpha calculation with 1 dp")
        PiUtility.init_pi(PiAlgorithmType.BBP, 12)
        alpha = AlgorithmRunner.calculate_alpha(AlphaAlgorithmType.Newton, 1)
        self.assertTrue(almosteq(alpha, mpmathify("2.3098814600", strings=True), 1e-1))
        print("=======================")

    def test_alpha_5dp_precision(self):
        """Checking the accuracy of the calculation : 5 dp."""
        print("Test of alpha calculation with 5 dp")
        PiUtility.init_pi(PiAlgorithmType.BBP, 12)
        alpha = AlgorithmRunner.calculate_alpha(AlphaAlgorithmType.Newton, 5)
        self.assertTrue(almosteq(alpha, mpmathify("2.3098814600", strings=True), 1e-5))
        print("=======================")

    def test_alpha_20dp_precision(self):
        """Checking the accuracy of the calculation : 20 dp."""
        print("Test of alpha calculation with 20 dp")
        PiUtility.init_pi(PiAlgorithmType.BBP, 20)
        alpha = AlgorithmRunner.calculate_alpha(AlphaAlgorithmType.Newton, 20)
        self.assertTrue(almosteq(alpha, mpmathify("2.3098814600100572608867", strings=True), 1e-20))
        print("=======================")

    def test_alpha_0dp_precision(self):
        """Checking the return value if the precision is equal to 0.
        
            Return:
                The calculation result must be the same as initial value which
                is 2.5. The test checks the return value against 2.5
        """
        print("Test of alpha calculation with the precision equal to 0.")
        PiUtility.init_pi(PiAlgorithmType.BBP, 0)
        alpha = AlgorithmRunner.calculate_alpha(AlphaAlgorithmType.Newton, 0)
        self.assertEqual(alpha, mpf(2.5))
        print("=======================")

    def test_alpha_negative_precision(self):
        """Checking the return value if the precision is negative.
        
            Return:
                The calculation result must be the same as initial value which
                is 2.5. The test checks the return value against 2.5
        """
        print("Test of alpha calculation with negative precision.")
        PiUtility.init_pi(PiAlgorithmType.BBP, -2)
        alpha = AlgorithmRunner.calculate_alpha(AlphaAlgorithmType.Newton, -2)
        self.assertEqual(alpha, mpf(2.5))
        print("=======================")


if __name__ == '__main__':
    unittest.main()