# 2239. Find Closest Number to Zero

Given an integer array `nums` of size `n`, return the number with the value closest to `0` in `nums`. If there are multiple answers, return the number with the largest value.

## Example 1:

**Input:** nums = `[-4,-2,1,4,8]`
**Output:** `1`
**Explanation:**
The distance from -4 to 0 is `|-4| = 4`.
The distance from -2 to 0 is `|-2| = 2`.
The distance from 1 to 0 is `|1| = 1`.
The distance from 4 to 0 is `|4| = 4`.
The distance from 8 to 0 is `|8| = 8`.
Thus, the closest number to 0 is 1.

## Example 2:

**Input:** nums = `[2,-1,1]`
**Output:** `1`
**Explanation:**
Both 1 and -1 are the closest numbers to 0, so the largest value 1 is returned.

## Constraints:

*   `1 <= n <= 1000`
*   `-10^5 <= nums[i] <= 10^5`

---

## Solution Explanation

The solution uses Python's built-in `min()` function with a custom sorting key provided by a `lambda` function.

`return min(nums, key=lambda x: (abs(x), -x))`

### Logic

When you provide a `key` to the `min()` function, it doesn't compare the items in the list directly. Instead, it calls the key function on each item and compares the return values.

In this case, the key `lambda x: (abs(x), -x)` returns a tuple `(distance_from_zero, negative_value)` for each number `x` in the list.

Python compares tuples element by element. 

1.  It first compares the first element of the tuples: `abs(x)`. This finds the number(s) with the smallest distance from zero.
2.  If there is a tie (e.g., for `1` and `-1`, the `abs(x)` is `1` for both), Python moves to the second element of the tuple to break the tie: `-x`.
3.  The `min()` function will choose the smaller of these second elements. To get the *largest* number in a tie (as the problem requires), we compare their negatives. For `1` and `-1`, the second tuple elements are `-1` and `1` respectively. `min(-1, 1)` is `-1`, which corresponds to the original number `1`. This is how the tie is broken in favor of the larger value.

### Complexity

*   **Time Complexity: O(n)**
    The `min()` function must iterate through all `n` elements of the input list `nums` once to find the minimum value based on the provided key. Therefore, the time complexity is linear.

*   **Space Complexity: O(1)**
    The solution uses a constant amount of extra space. It does not create any new data structures that scale with the size of the input list. The `min` operation only needs to keep track of the minimum element found so far.