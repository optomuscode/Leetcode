from typing import List

class Solution:
  def findClosestNumber(self, nums: List[int]) -> int:
    """
    Finds the number in the list closest to zero.

    Args:
      nums: A list of integers.

    Returns:
      The integer closest to zero. If there is a tie, the larger number is returned.
    """
    return min(nums, key=lambda x: (abs(x), -x))
