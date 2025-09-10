# 682. Baseball Game

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings `operations`, where `operations[i]` is the ith operation you must apply to the record and is one of the following:

*   An integer `x`: Record a new score of `x`.
*   `'+'`: Record a new score that is the sum of the previous two scores.
*   `'D'`: Record a new score that is double the previous score.
*   `'C'`: Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

## Example 1:

**Input:** ops = ["5","2","C","D","+"]
**Output:** 30
**Explanation:**
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.

## Example 2:

**Input:** ops = ["5","-2","4","C","D","9","+","+"]
**Output:** 27
**Explanation:**
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

## Constraints:

*   `1 <= operations.length <= 1000`
*   `operations[i]` is `"C"`, `"D"`, `"`, or a string representing an integer in the range `[-3 * 10^4, 3 * 10^4]`.
*   For operation `"+"`, there will always be at least two previous scores on the record.
*   For operations `"` and `"D"`, there will always be at least one previous score on the record.

---

## Intuition

The problem requires us to manage a sequence of scores where operations depend on the most recent valid scores. The operations "C" (undo), "D" (double the last score), and "+" (sum of the last two scores) all relate to the end of the sequence. This "Last-In, First-Out" (LIFO) behavior is a strong indicator that a **stack** is the ideal data structure for this problem.

## Approach

We can process the `operations` list one by one, using a stack (which can be implemented with a Python list) to maintain the record of valid scores.

1.  **Initialize a Stack**: Create an empty list, `stk`, to function as our stack.
2.  **Iterate Through Operations**: Loop through each `op` in the input `operations` list.
3.  **Process Each Operation**:
    *   If `op` is `"+"`, we access the last two elements of the stack (`stk[-1]` and `stk[-2]`), sum them up, and push the result back onto the stack.
    *   If `op` is `"D"`, we take the last element (`stk[-1]`), double it, and push the result onto the stack.
    *   If `op` is `"C"`, we simply pop the last element from the stack, effectively invalidating it.
    *   Otherwise, the `op` is a number. We convert it to an integer and push it onto the stack.
4.  **Calculate Final Sum**: After iterating through all operations, the stack will contain all the valid scores. The final result is the sum of all elements in the stack.

### Visual Logic

```mermaid
flowchart TD
    A[Start] --> B[Initialize empty stack `stk`];
    B --> C{Loop through `operations`};
    C -- op --> D{Is `op` a command?};
    D -- Yes --> E{What command?};
    D -- No --> F[Convert `op` to int];
    F --> G[Push to `stk`];
    G --> C;

    E -- "+" --> H[sum = stk[-1] + stk[-2]];
    H --> I[Push `sum` to `stk`];
    I --> C;

    E -- "D" --> J[doubled = stk[-1] * 2];
    J --> K[Push `doubled` to `stk`];
    K --> C;

    E -- "C" --> L[Pop from `stk`];
    L --> C;

    C -- End of Loop --> M[Sum all elements in `stk`];
    M --> N[Return sum];
    N --> O[End];
```

## Complexity

Let `N` be the number of operations in the input list.

*   **Time Complexity: O(N)**
    We iterate through the `operations` list once. Each operation (push, pop, accessing the end of the list) takes constant time on average. Therefore, the time complexity is linear with respect to the number of operations.

*   **Space Complexity: O(N)**
    In the worst-case scenario, none of the operations are "C", and we keep adding numbers to the stack. The stack could grow to a size of `N`. Therefore, the space required is also linear with respect to the number of operations.

## Key Learnings

*   **Stack for LIFO**: This problem is a classic example of when to use a stack. Recognizing the LIFO (Last-In, First-Out) nature of the operations is key to finding an efficient solution.
*   **Direct Simulation**: Sometimes, the most straightforward approach is to directly simulate the process described in the problem statement. The stack allows for a clean and direct simulation of the game's rules.
*   **List as a Stack**: In Python, lists provide all the necessary methods (`append` for push, `pop` for pop) to be used effectively as a stack.
