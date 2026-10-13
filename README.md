# Coding Assignment 3

## Introduction

This repository contains solutions for CS526 Homework Assignment 3.

---

## Algorithm

### Problem 1: Palindrome

The algorithm cleans the input string by removing single-space separators while preserving character case[cite: 7]. It then compares the cleaned string directly to its reverse using string slicing (`s[::-1]`). If both match, it returns `True` and increments the total palindrome count; otherwise, it returns `False` [cite: 7]. The program processes input line by line until all lines are evaluated[cite: 7].

### Problem 2: Substrings

The algorithm recursively generates all consecutive character runs without using loops[cite: 7]. A recursive helper expands the substring slice from a starting index to an ending index, storing each generated substring in a set to automatically eliminate duplicates[cite: 7]. Once the ending boundary reaches the string length, the start index increments to search the next character position. Finally, the set of unique substrings is sorted alphabetically and printed alongside the total count[cite: 7].

### Problem 3: Reverse Stack

The algorithm reverses three stack implementations in-place using recursion without loops[cite: 7]. A main recursive function repeatedly pops the top element off the stack until it becomes empty, holding all values in the call stack. A recursive helper function, `insert_at_bottom`, then inserts each popped item at the base of the emptied stack. As the call stack unwinds, elements are pushed back in reverse order.

### Problem 4: Ghostbusters

The algorithm checks whether any streams cross by testing if all Ghostbuster-ghost directional vectors are parallel and non-collinear[cite: 7]. It uses integer 2D cross-products to determine if two line vectors share the exact same direction without floating-point precision loss. If two streams have different direction slopes or lie on the exact same line, they cross, and the algorithm outputs that ghosts were not eliminated[cite: 7]. All ghosts are eliminated only if every stream is strictly parallel and distinct[cite: 7].

---

## Interesting Aspects

- **Zero-Tolerance Stream Collisions:** In Problem 4, collinear streams (two different Ghostbuster-ghost pairs firing along the exact same straight line) are treated as crossing, causing immediate failure[cite: 7]. This edge case requires checking not only if direction vectors are parallel, but also verifying that no two streams share a line origin via non-collinear point testing.
- **Space-Preserving Palindrome Logic:** In Problem 1, space removal strips single space separators without altering character case[cite: 7]. This allows strings with spaced characters (e.g., `"g e e k"`) to be evaluated cleanly against strict case-sensitive palindrome rules[cite: 7].
- **In-Place Call-Stack Reversal:** In Problem 3, stack reversal operates strictly in-place without instantiating secondary data structures[cite: 7]. By leveraging the execution call stack through double recursion (`reverse_stack` and `insert_at_bottom`), elements are unwound and placed at the base, reversing array-based, singly linked, and doubly linked stacks seamlessly without loops[cite: 7].

---

## How to Run

### Problem 1: Palindrome

Run the script against test input files using standard input redirection:

```bash
python3 palindrome.py < problem1_res/palindrome_0.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_0L.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_0S.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_1.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_1L.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_1S.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_2.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_2L.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_2S.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_3.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_3L.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_3S.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_4.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_4L.txt
```

```bash
python3 palindrome.py < problem1_res/palindrome_4S.txt
```

### Problem 2: Substrings

Run the script against test input files using standard input redirection:

```bash
python3 substrings.py < problem2_res/unique_substrings_input_0.txt
```

```bash
python3 substrings.py < problem2_res/unique_substrings_input_1.txt
```

```bash
python3 substrings.py < problem2_res/unique_substrings_input_2.txt
```

### Problem 3: Reverse Stack

Execute the recursive combination script directly:

```bash
python3 problem3.py
```

### Problem 4: Ghostbusters

Run the script against test input files using standard input redirection:

```bash
python3 ghostbusters.py < problem4_res/ghostbusters_input_0.txt
```

```bash
python3 ghostbusters.py < problem4_res/ghostbusters_input_1.txt
```

```bash
python3 ghostbusters.py < problem4_res/ghostbusters_input_2.txt
```

```bash
python3 ghostbusters.py < problem4_res/ghostbusters_input_3.txt
```

```bash
python3 ghostbusters.py < problem4_res/ghostbusters_input_4.txt
```

```bash
python3 ghostbusters.py < problem4_res/ghostbusters_input_5.txt
```

```bash
python3 ghostbusters.py < problem4_res/ghostbusters_input_6.txt
```

```bash
python3 ghostbusters.py < problem4_res/ghostbusters_input_7.txt
```

```bash
python3 ghostbusters.py < problem4_res/ghostbusters_input_8.txt
```

```bash
python3 ghostbusters.py < problem4_res/ghostbusters_input_9.txt
```

```bash
python3 ghostbusters.py < problem4_res/ghostbusters_input_10.txt
```
