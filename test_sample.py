import unittest

from src import sample

class TestSampleMethod(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(10, sample.inc(9))
    def test_upper2(self):
        self.assertEqual(0, sample.inc(-1))
    def test_upper3(self):
        self.assertEqual(3, sample.inc(1))

if __name__ == '__main__':
    unittest.main()
