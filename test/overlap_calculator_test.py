import _src_path
from mpmath import nstr, mpf
from overlap_calculator.overlap_calculator import OverlapCalculator

length = OverlapCalculator.calculate_overlapping_length(20)
print("Overlapping length :", nstr(length, 15))

length = OverlapCalculator.calculate_overlapping_length(20000000000)
print("Overlapping length :", nstr(length, 15))

length = OverlapCalculator.calculate_overlapping_length(mpf(0.0003))
print("Overlapping length :", nstr(length, 15))