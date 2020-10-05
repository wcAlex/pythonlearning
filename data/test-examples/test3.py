import unittest
from . import simple_math

class MyTest(unittest.TestCase):

    def test_one_and_one(self):
        self.assertEqual(simple_math.add(1, 1), 2)

    def test_one_and_one_fail(self):
        self.assertEqual(simple_math.add(1, 1), 4)

    def test_one_and_one_fail_assert(self):
        assert simple_math.add(1,1) == 4

    def test_lists(self):
        self.assertEquals([1, 2, 4], [1, 2, 3, 4])
