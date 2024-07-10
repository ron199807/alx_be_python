import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
        def setUp(self):
            self.calculator = SimpleCalculator()

        def test_addition(self):
            self.assertEqual(self.calculator.add(2, 3), 5)
            self.assertEqual(self.calculator.add(-1, 1), 0)
            self.assertEqual(self.calculator.add(-1, -1), -2)
            self.assertEqual(self.calculator.add(0, 0), 0)
        
        def test_subtraction(self):
            self.assertEqual(self.calculator.test_subtract(3, 2), 1)
            self.assertEqual(self.calculator.test_subtract(-1, 1), -2)
            self.assertEqual(self.calculator.test_subtract(-1, -1), 0)
            self.assertEqual(self.calculator.test_subtract(0, 0), 0)

        def test_multiplication(self):
            self.assertEqual(self.calculator.test_multiply(3, 2), 6)
            self.assertEqual(self.calculator.test_multiply(-1, 1), -1)
            self.assertEqual(self.calculator.test_multiply(-1, -1), 1)
            self.assertEqual(self.calculator.test_multiply(0, 1), 0)

        def test_division(self):
            self.assertEqual(self.calculator.test_divide(6, -2), 3)
            self.assertEqual(self.calculator.test_divide(-6, 2), -3)
            self.assertEqual(self.calculator.test_divide(-6, -2), 3)
            self.assertEqual(self.calculator.test_divide(0, -1), 0)
            self.assertIsNone(self.calculator.test_divide(1, 0), "Division by zeroshould return None")

if __name__ == "__main__":
    unittest.main()

        
