import _src_path
from mpmath import nstr
from overlap_calculator.alpha_calculator.algorithm_runner import AlgorithmRunner, AlgorithmType


for precision in range(1 , 40):
    alpha = AlgorithmRunner.calculate_alpha(AlgorithmType.Newton, precision)
    print(precision, "-iter alpha is:  ", nstr(alpha, precision + 1))