import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_subtract(self):
        result = self.calc.subtract(9, 3)
        self.assertEqual(result, 6)
    
    def test_multiply(self):
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)
    
    def test_divide_normal(self):
        result = self.calc.divide(6, 3)
        self.assertEqual(result, 2)

    def test_divide_Zero(self):
        result = self.calc.divide(6, 0)
        self.assertEqual(result, None)
    


if __name__ == "__main__":
    unittest.main()
