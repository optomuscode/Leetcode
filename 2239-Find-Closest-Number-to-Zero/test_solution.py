import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        self.assertEqual(self.solver.findClosestNumber([-4, -2, 1, 4, 8]), 1)

    def test_example_2(self):
        self.assertEqual(self.solver.findClosestNumber([2, -1, 1]), 1)

    def test_single_positive(self):
        self.assertEqual(self.solver.findClosestNumber([5]), 5)

    def test_single_negative(self):
        self.assertEqual(self.solver.findClosestNumber([-5]), -5)

    def test_zero(self):
        self.assertEqual(self.solver.findClosestNumber([0]), 0)

    def test_all_positives(self):
        self.assertEqual(self.solver.findClosestNumber([1, 2, 3, 4, 5]), 1)

    def test_all_negatives(self):
        self.assertEqual(self.solver.findClosestNumber([-1, -2, -3, -4, -5]), -1)

    def test_tiebreaker(self):
        self.assertEqual(self.solver.findClosestNumber([-10, 10]), 10)

    def test_mixed_numbers(self):
        self.assertEqual(self.solver.findClosestNumber([-100, -50, 50, 100]), 50)

if __name__ == '__main__':
    unittest.main()
