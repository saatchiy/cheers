import _src_path
from utils.pi.pi_util import PiUtility, AlgorithmType

# A test for calculation of PI number with default precision
calculated_pi = PiUtility.pi(AlgorithmType.BBP)
print("Calculated PI value is: ", calculated_pi)

# PI should not be re-calculated since the precision is the same
calculated_pi = PiUtility.pi(AlgorithmType.BBP, 3)
print("Calculated PI value is: ", calculated_pi)

# PI should be re-calculated because the desired precision in changed
calculated_pi = PiUtility.pi(AlgorithmType.BBP, 4)
print("Calculated PI value is: ", calculated_pi)

# PI should not be re-calculated
calculated_pi = PiUtility.pi(AlgorithmType.BBP, 4)
print("Calculated PI value is: ", calculated_pi)