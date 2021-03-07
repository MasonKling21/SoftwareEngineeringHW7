import unittest
from fizzBuzz import *

class TestFunction(unittest.TestCase):
    def test_fizzBuzz(self):
        self.assertEqual(fizzedBuzz(3), "Fizz")
        self.assertEqual(fizzedBuzz(5), "Buzz")
        self.assertEqual(fizzedBuzz(15), "FizzBuzz")
        self.assertEqual(fizzedBuzz(16), 16)
        self.assertEqual(fizzedBuzz("a"), "Error!")


if __name__ == "__main__":
    unittest.main()
