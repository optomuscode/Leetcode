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

## Intuition

The problem asks us to find a number in an array that is closest to zero. This means we need to compare the absolute distances of each number from zero. A key detail is the tie-breaking rule: if two numbers are equally close to zero (e.g., -5 and 5), we should return the larger of the two. This implies that simply finding the minimum absolute value isn't enough; we need a secondary comparison for ties.

## Approach

We can solve this problem by iterating through the array and keeping track of the number that is currently closest to zero.

1.  **Initialization**: Start by assuming the first number in the array (`nums[0]`) is the `closest_num` found so far, and its absolute value (`abs(nums[0])`) is the `min_dist`.

2.  **Iteration**: Loop through the rest of the numbers in the array (starting from the second element). For each `current_num`:
    *   Calculate its `current_dist` from zero (`abs(current_num)`).
    *   **Comparison**:
        *   If `current_dist` is less than `min_dist`: This `current_num` is strictly closer to zero. Update `min_dist` to `current_dist` and `closest_num` to `current_num`.
        *   If `current_dist` is equal to `min_dist`: We have a tie. According to the problem, we should choose the larger number. So, if `current_num` is greater than `closest_num`, update `closest_num` to `current_num`.
        *   If `current_dist` is greater than `min_dist`: This `current_num` is further away, so we do nothing.

3.  **Return**: After iterating through all numbers, `closest_num` will hold the number closest to zero, correctly handling ties.

### Visual Logic

This flowchart illustrates the explicit approach.

```mermaid
flowchart TD
    A[Start] --> B{Initialize closest_num = nums[0], min_dist = abs(nums[0])};
    B --> C{For each num in nums (from second element)};
    C -- Yes --> D{Calculate current_dist = abs(num)};
    D --> E{Is current_dist < min_dist?};
    E -- Yes --> F[min_dist = current_dist, closest_num = num];
    F --> C;
    E -- No --> G{Is current_dist == min_dist?};
    G -- Yes --> H{Is num > closest_num?};
    H -- Yes --> I[closest_num = num];
    I --> C;
    H -- No --> C;
    G -- No --> C;
    C -- No --> J[Return closest_num];
    J --> K[End];
```

## Complexity

Let `N` be the number of elements in the `nums` array.

*   **Time Complexity: O(N)**
    *   The algorithm iterates through the `nums` array exactly once. Each operation inside the loop (absolute value calculation, comparisons, assignments) takes constant time. Therefore, the total time complexity is directly proportional to the number of elements in the input array.

*   **Space Complexity: O(1)**
    *   The algorithm uses a fixed amount of extra space for variables like `closest_num`, `min_dist`, `num`, and `dist`. This space does not grow with the size of the input array.

## Key Learnings

*   **Iterative Tracking**: This problem demonstrates a common pattern of iterating through a collection and maintaining a "best so far" value based on specific criteria.
*   **Tie-Breaking Logic**: It highlights the importance of carefully handling edge cases and tie-breaking rules, which often require secondary conditions in comparison logic.
*   **Absolute Value**: Reinforces the use of absolute values when distance from zero (or any point) is the primary concern.
*   **Clarity vs. Conciseness**: While a one-liner solution exists (using `min` with a custom key), the explicit iterative approach can sometimes be more readable and easier to debug for those unfamiliar with advanced Python features or complex `key` functions. Both have their place depending on context.
