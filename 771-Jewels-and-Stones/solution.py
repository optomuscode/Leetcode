class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Counts how many of the stones are also jewels.

        Args:
            jewels: A string where each character is a distinct type of jewel.
            stones: A string representing the stones you have.

        Returns:
            The count of stones that are also jewels.
        """
        jewel_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        return count
