import unittest
from pi_calculation_test import TestPi
from alpha_calculator_test import TestAlphaCalculation
from overlap_calculator_test import TestOverlapCalculation

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestPi))
    test_suite.addTest(unittest.makeSuite(TestAlphaCalculation))
    test_suite.addTest(unittest.makeSuite(TestOverlapCalculation))

    result = runner.run(test_suite)

    print("---- START OF TEST RESULTS")
    print(result)
    print("result::errors")
    print(result.errors)
    print("result::failures")
    print(result.failures)
    print("result::skipped")
    print(result.skipped)
    print("result::successful")
    print(result.wasSuccessful())
    print("result::test-run")
    print(result.testsRun)
    print("---- END OF TEST RESULTS")