import unittest
from fizzBuzz import *
from leapYear import *

class TestFunction(unittest.TestCase):
    def test_fizzBuzz(self):
        self.assertEqual(fizzedBuzz(3), "Fizz")
        self.assertEqual(fizzedBuzz(5), "Buzz")
        self.assertEqual(fizzedBuzz(15), "FizzBuzz")
        self.assertEqual(fizzedBuzz(16), 16)
        self.assertEqual(fizzedBuzz("a"), "Error!")

    def test_leapYear(self):
        self.assertEqual(leapYear(4), "Leap year")
        self.assertEqual(leapYear(100), "Not a leap year")
        self.assertEqual(leapYear(400), "Leap year")


if __name__ == "__main__":
    unittest.main()
