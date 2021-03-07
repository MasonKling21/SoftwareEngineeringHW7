import unittest
from fizzBuzz import *

class TestFunction(unittest.TestCase):
    def test_fizzBuzz(self):
        self.assertEqual(fizzedBuzz(3), "Fizz")
        self.assertEqual(fizzedBuzz(5), "Buzz")


if __name__ == "__main__":
    unittest.main()
