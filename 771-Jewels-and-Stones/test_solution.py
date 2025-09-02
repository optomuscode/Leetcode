import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        self.assertEqual(self.solver.numJewelsInStones(jewels="aA", stones="aAAbbbb"), 3)

    def test_example_2(self):
        self.assertEqual(self.solver.numJewelsInStones(jewels="z", stones="ZZ"), 0)

    def test_no_jewels(self):
        self.assertEqual(self.solver.numJewelsInStones(jewels="", stones="aAAbbbb"), 0)

    def test_no_stones(self):
        self.assertEqual(self.solver.numJewelsInStones(jewels="aA", stones=""), 0)

    def test_all_jewels(self):
        self.assertEqual(self.solver.numJewelsInStones(jewels="abc", stones="abacaba"), 7)

    def test_no_matches(self):
        self.assertEqual(self.solver.numJewelsInStones(jewels="xyz", stones="abcdefg"), 0)

    def test_case_sensitivity(self):
        self.assertEqual(self.solver.numJewelsInStones(jewels="a", stones="A"), 0)

if __name__ == '__main__':
    unittest.main()
