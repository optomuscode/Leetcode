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
    # Explicit Solution
    closest_num = nums[0]
    min_dist = abs(nums[0])

    for i in range(1, len(nums)):
      num = nums[i]
      dist = abs(num)

      if dist < min_dist:
        min_dist = dist
        closest_num = num
      elif dist == min_dist:
        if num > closest_num: # Tie-breaker: return the larger number
          closest_num = num
    
    return closest_num

    # --- One-liner equivalent (for conciseness) ---
    # This solution leverages Python's min() function with a custom key.
    # The key (abs(x), -x) sorts by absolute value first, then by the negative
    # of the number (which effectively sorts by the number itself in descending order
    # for tie-breaking, thus picking the larger number).
    # return min(nums, key=lambda x: (abs(x), -x))