import unittest
from calplus import sumInt
class CalTestCase(unittest.TestCase):
    def test_calplus(self):
        result = sumInt(12, 17)
        self.assertEqual(result, 29)

unittest.main()
