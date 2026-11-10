# Coding Assignment 5

## Introduction

This repository contains solutions for CS526 Homework Assignment 5. The assignment covers binary search trees, dynamic programming on strings, and dynamic programming over two sequences. The implementations build a BST ADT with add, delete, find, and print operations. They also count how many ways a dot/dash sequence can be decoded into Morse-code vowels, and find the longest increasing sequence that alternates between two arrays under a position constraint.

---

## Algorithm

### Problem 1: Binary Search Tree

The algorithm implements a binary search tree, where each node holds a value and every value in its left subtree is smaller, and every value in its right subtree is larger (duplicates are ignored). `add_node` walks down from the root, going left or right by comparison, and inserts a new leaf at the first empty spot. `find_node` follows the same left/right path and returns `True` if it hits a matching value or `False` if it runs off the tree. `delete_node` handles three cases: a leaf is removed, a node with one child is replaced by that child, and a node with two children copies the value of its in-order successor (the smallest value in its right subtree) and then deletes that successor, which keeps the ordering intact. `print_tree` does an in-order traversal, so it prints the values in sorted order rather than showing the tree’s shape. The demo seeds the random generator with 42, generates 5 to 50 unique numbers between 1 and 1000, and builds the tree from them. It then prints the tree after adding one random value and after deleting the first input value, and finally searches for one value that exists and one (9999) that doesn’t.

### Problem 2: Vowel Combination (Morse Code)

The algorithm counts how many ways a sequence of dots and dashes can be split into Morse codes for vowels only: A `.-`, E `.`, I `..`, O `---`, U `..-`. It uses dynamic programming. Let `dp[i]` be the number of ways to decode the first $i$ symbols, with `dp[0] = 1` for the empty prefix. For each $i$, it checks every vowel code that ends at position $i$ and adds `dp[i - len(code)]`. The answer is `dp[n]`. Every decoding is counted exactly once, because each one has a unique last vowel, which defines a unique smaller subproblem. The running time is $O(n)$, since there are only 5 codes to check per position.

### Problem 3: Longest Sequence

The algorithm finds the longest sequence $X$ with strictly increasing values whose elements alternate between arrays $A$ and $B$. Each element’s position in its own array must also be strictly greater than the position of the previous element in its array. This is why $\{1, 4, 7\}$ is invalid in the spec’s example while $\{4, 7, 9\}$ is valid.

The solution uses dynamic programming with two tables:

- `fa[i]` is the length of the longest valid sequence ending at $A[i]$.
- `fb[j]` is the length of the longest valid sequence ending at $B[j]$.

$A[i]$ can extend a sequence ending at $B[j]$ only if $j < i$ and $B[j] < A[i]$, so $\text{fa}[i] = 1 + \max(\text{fb}[j])$ over all such $j$, or $1$ if none exist. `fb[j]` is computed the same way from $A$. The answer is the maximum value across both tables. Predecessor pointers are stored so one optimal sequence can be rebuilt (shown with `--show`). The running time is $O(n \cdot m)$ and the space is $O(n + m)$.

---

## Interesting Aspects

- **Three-case deletion in the BST:** Replacing a two-child node with its in-order successor removes it without restructuring the tree. The in-order traversal stays sorted, which I checked after 100 random deletions from a 200-node tree.
- **Counting decodings without enumerating them:** Problem 2 has exponentially many possible splits, but the DP counts them in $O(n)$ time using Python’s arbitrary-size integers. This handles large results such as 193050000 without overflow.
- **The cross-array position constraint:** Problem 3 is not a standard longest-increasing-subsequence problem, because positions in $A$ and $B$ are compared with each other. Requiring $j < i$ turns the transition into a simple loop over earlier positions. I verified the DP against a brute-force search on 300 random small inputs, and it matched every time.

---

## How to Run

### Problem 1: Binary Search Tree

Run the script directly to execute the randomized BST operations demonstration:

```bash
python3 binary_search_tree.py
```

### Problem 2: Vowel Combination (Morse Code)

Run the script against test input files:

```bash
python3 vowel_combination.py problem2_res/vowel_input1.txt
```

```bash
python3 vowel_combination.py problem2_res/vowel_input2.txt
```

```bash
python3 vowel_combination.py problem2_res/vowel_input3.txt
```

```bash
python3 vowel_combination.py problem2_res/vowel_input4.txt
```

### Problem 3: Longest Sequence

Run the script against test input files:

```bash
python3 longest_sequence.py problem3_res/longest_seq1.txt
```

```bash
python3 longest_sequence.py problem3_res/longest_seq2.txt
```

```bash
python3 longest_sequence.py problem3_res/longest_seq3.txt
```

```bash
python3 longest_sequence.py problem3_res/longest_seq4.txt
```

```bash
python3 longest_sequence.py problem3_res/longest_seq5.txt
```

```bash
python3 longest_sequence.py problem3_res/longest_seq6.txt
```
