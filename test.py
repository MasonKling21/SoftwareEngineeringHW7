import unittest
from fizzBuzz import *

class TestFunction(unittest.TestCase):
    def test_fizzBuzz(self):
        self.assertEqual(fizzedBuzz(3), "Fizz")


if __name__ == "__main__":
    unittest.main()
