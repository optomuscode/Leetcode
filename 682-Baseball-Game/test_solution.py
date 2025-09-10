import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        self.assertEqual(self.solver.calPoints(["5","2","C","D","+"]), 30)

    def test_example_2(self):
        self.assertEqual(self.solver.calPoints(["5","-2","4","C","D","9","+","+"]), 27)

    def test_example_3(self):
        self.assertEqual(self.solver.calPoints(["1"]), 1)

if __name__ == '__main__':
    unittest.main()