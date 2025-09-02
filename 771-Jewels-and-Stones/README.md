# 771. Jewels and Stones

You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

## Example 1:

**Input:** jewels = "aA", stones = "aAAbbbb"
**Output:** 3

## Example 2:

**Input:** jewels = "z", stones = "ZZ"
**Output:** 0

## Constraints:

*   `1 <= jewels.length, stones.length <= 50`
*   `jewels` and `stones` consist of English letters.
*   The characters in `jewels` are distinct.

---

## Solution Explanation

The most efficient way to solve this problem is to use a **Hash Set** (or simply a `set` in Python). The goal is to check for the existence of each stone in our collection of jewels quickly.

1.  **Build the Jewel Set**: First, we convert the `jewels` string into a hash set. A hash set provides near-instantaneous lookups (average O(1) time complexity). This is much more efficient than repeatedly scanning the `jewels` string.

2.  **Iterate and Count**: Next, we iterate through each character in the `stones` string. For each `stone`, we check if it exists in our `jewel_set`.

3.  **Increment**: If the stone is found in the `jewel_set`, we increment a counter.

After checking all the stones, the final count is our answer.

### Visual Logic

This flowchart illustrates the process using the example `jewels = "aA"` and `stones = "aAAbbbb"`.

```mermaid
flowchart TD
    A[Start] --> B{Create jewel_set from 'aA'};
    B --> C[jewel_set = {'a', 'A'}];
    C --> D[Initialize count = 0];
    D --> E{Loop through each stone in 'aAAbbbb'};
    E --> F{stone = 'a'};
    F --> G{{Is 'a' in jewel_set?}};
    G -- Yes --> H[count = 1];
    H --> I{stone = 'A'};
    I --> J{{Is 'A' in jewel_set?}};
    J -- Yes --> K[count = 2];
    K --> L{stone = 'A'};
    L --> M{{Is 'A' in jewel_set?}};
    M -- Yes --> N[count = 3];
    N --> O{stone = 'b'};
    O --> P{{Is 'b' in jewel_set?}};
    P -- No --> Q{...and so on for remaining 'b's...};
    Q --> R[End Loop];
    R --> S[Return count: 3];
    S --> T[End];
```

### Complexity

Let `J` be the length of the `jewels` string and `S` be the length of the `stones` string.

*   **Time Complexity: O(J + S)**
    *   It takes O(J) time to build the hash set from the `jewels` string.
    *   It then takes O(S) time to iterate through the `stones` string. For each stone, the lookup in the hash set is, on average, an O(1) operation.
    *   Therefore, the total time complexity is O(J + S).

*   **Space Complexity: O(J)**
    *   We use a hash set to store the unique jewels. In the worst case, all characters in `jewels` are unique, so the space required for the set is proportional to the length of the `jewels` string.