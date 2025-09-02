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
        
        # Intuition: To efficiently check if a stone is a jewel, 
        # we need a fast way to look up jewel types. A set provides O(1) average time complexity for lookups.

        # Step 1: Create a set of jewels for efficient lookup
        jewel_types = set()
        for char in jewels:
            jewel_types.add(char)

        # Step 2: Initialize a counter for jewels found
        count = 0

        # Step 3: Iterate through each stone and check if it's a jewel
        for stone in stones:
            if stone in jewel_types:
                count += 1

        # Step 4: Return the total count of jewels found
        return count

        # --- One-liner equivalent (for conciseness) ---
        # This solution leverages a set comprehension and sum to count jewels.
        # It first creates a set of jewels for O(1) average time lookups,
        # then sums 1 for each stone that is found in the jewel set.
        # return sum(s in set(jewels) for s in stones)
