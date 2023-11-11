import unittest
from my_calculations import Calculations


class TestCalculations(unittest.TestCase):

    def setUp(self) -> None:
        self.calculation = Calculations(8, 2)

    def test_sum(self):
        
        self.assertEqual(self.calculation.get_sum(), 10, 'The sum is wrong.')

    def test_diff(self):
        
        self.assertEqual(self.calculation.get_difference(), 6, 'The difference is wrong.')

    def test_product(self):
        
        self.assertEqual(self.calculation.get_product(), 16, 'The product is wrong.')

    def test_quotient(self):
        
        self.assertEqual(self.calculation.get_quotient(), 4, 'The quotient is wrong.')


if __name__ == '__main__':
    unittest.main()



# command line:  python3 -m unittest  - RUN THE TEST IN ALL FILES IN THIS DRCTORY
#                python3 -m unittest test.py - RUN THE TEST IN THIS FILE

#                python3 -m unittest - v  - The -v makes the output a bit more verbose, which can be useful when running several tests at once:
# test_diff (test.TestCalculations) ... ok
# test_product (test.TestCalculations) ... ok
# test_quotient (test.TestCalculations) ... ok
# test_sum (test.TestCalculations) ... ok
# test_isupper (test_str.TestStringMethods) ... ok
# test_split (test_str.TestStringMethods) ... ok
# test_upper (test_str.TestStringMethods) ... ok


                # python -m unittest -v tests.test.TestCalculations.test_diff  - RUN ONE METHOD IN ONE FILE
                 