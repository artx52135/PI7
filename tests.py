import main
import unittest

class TestArabicToRoman(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(25))
        self.assertTrue(is_prime(29))


