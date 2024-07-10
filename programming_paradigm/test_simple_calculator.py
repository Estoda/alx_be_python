import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(9, 3), 6)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
    
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_divide_Zero(self):
        self.assertEqual(self.calc.divide(6, 0), None)
    


if __name__ == "__main__":
    unittest.main()
