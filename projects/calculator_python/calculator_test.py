import unittest
from projects.calculator_python.calculator import Calculator

class TestSum(unittest.TestCase):
    def test_sum(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2,1),4)


if __name__ == "__main__":
    unittest.main()

