import unittest
from mpmath import *
import _src_path
from utils.pi.pi_util import PiUtility, AlgorithmType

# # A test for calculation of PI number with default precision
# calculated_pi = PiUtility.pi(AlgorithmType.BBP)
# print("Calculated PI value is: ", calculated_pi)

# # PI should not be re-calculated since the precision is the same
# calculated_pi = PiUtility.pi(AlgorithmType.BBP, 3)
# print("Calculated PI value is: ", calculated_pi)

# # PI should be re-calculated because the desired precision in changed
# calculated_pi = PiUtility.pi(AlgorithmType.BBP, 4)
# print("Calculated PI value is: ", calculated_pi)

# # PI should not be re-calculated
# calculated_pi = PiUtility.pi(AlgorithmType.BBP, 4)
# print("Calculated PI value is: ", calculated_pi)

class TestPi(unittest.TestCase):

    def test_pi_10dp_accuracy(self):
        """Checking the accuracy of the calculation : 10 dp."""
        print("Test of Pi calculation with 10 decimal precision")
        PiUtility.init_pi(AlgorithmType.BBP, 10)
        my_pi = PiUtility.pi() 
        self.assertAlmostEqual(my_pi, mpf(3.14159265358), 10)
        print("=======================")

    def test_pi_10dp_precision(self):
        """Checking if the results repeat under the same conditions."""
        print("Test of Pi calculation with 10 decimal precision [repeat]")
        PiUtility.init_pi(AlgorithmType.BBP, 10)
        my_pi = PiUtility.pi() 
        self.assertAlmostEqual(my_pi, mpf(3.14159265358), 10)
        print("=======================")

    def test_pi_3dp_lower_accuracy(self):
        """Checking the calculation on lower accuracy : 3 dp."""
        print("Test of Pi calculation with 3 dp")
        PiUtility.init_pi(AlgorithmType.BBP, 3)
        my_pi = PiUtility.pi() 
        self.assertAlmostEqual(my_pi, mpf(3.14159265358), 3)
        print("=======================")

    def test_pi_20dp_higher_accuracy(self):
        """Checking the calculation on higher accuracy : 20 dp."""
        print("Test of Pi calculation with 20 dp")
        PiUtility.init_pi(AlgorithmType.BBP, 20)
        my_pi = PiUtility.pi()
        self.assertTrue(almosteq(my_pi, mpmathify("3.141592653589793238462", strings=True), 1e-20))
        print("=======================")

    def test_pi_negative_precision(self):
        """Checking the return value if the precision is negative.

            Return:
                Zero
        """
        print("Test of Pi calculation with negative decimal precision")
        PiUtility.init_pi(AlgorithmType.BBP, -2)
        my_pi = PiUtility.pi() 
        self.assertEqual(my_pi, mpf(0))
        print("=======================")

if __name__ == '__main__':
    unittest.main()