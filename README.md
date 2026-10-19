# Coding Assignment 4

## Introduction

This repository contains solutions for CS526 Homework Assignment 3. The assignment explores string processing algorithms, recursive sequence and substring generation, data structure reversals, and computational geometry applications. The provided Python modules implement a case-sensitive, space-insensitive palindrome checker, a recursive unique substring generator using set-based deduplication, a recursive stack reversal algorithm supporting array-based, singly linked, and doubly linked stack implementations, and an exact integer cross-product stream intersection solver for the Ghostbusters elimination problem.

---

## Algorithm

### Problem 1: A

The algorithm cleans the input string by removing single-space separators while preserving character case. It then compares the cleaned string directly to its reverse using string slicing (`s[::-1]`). If both match, it returns `True` and increments the total palindrome count; otherwise, it returns `False`. The program processes input line by line until all lines are evaluated.

### Problem 1: B

The algorithm recursively generates all consecutive character runs without using loops. A recursive helper expands the substring slice from a starting index to an ending index, storing each generated substring in a set to automatically eliminate duplicates. Once the ending boundary reaches the string length, the start index increments to search the next character position. Finally, the set of unique substrings is sorted alphabetically and printed alongside the total count.

### Problem 2: Smallest Number

The algorithm reverses three stack implementations in-place using recursion without loops. A main recursive function repeatedly pops the top element off the stack until it becomes empty, holding all values in the call stack. A recursive helper function, `insert_at_bottom`, then inserts each popped item at the base of the emptied stack. As the call stack unwinds, elements are pushed back in reverse order.

### Problem 3: Right Triangles

The algorithm checks whether any streams cross by testing if all Ghostbuster-ghost directional vectors are parallel and non-collinear. It uses integer 2D cross-products to determine if two line vectors share the exact same direction without floating-point precision loss. If two streams have different direction slopes or lie on the exact same line, they cross, and the algorithm outputs that ghosts were not eliminated. All ghosts are eliminated only if every stream is strictly parallel and distinct.

---

## Interesting Aspects

- **Zero-Tolerance Stream Collisions:** In Problem 4, collinear streams (two different Ghostbuster-ghost pairs firing along the exact same straight line) are treated as crossing, causing immediate failure. This edge case requires checking not only if direction vectors are parallel, but also verifying that no two streams share a line origin via non-collinear point testing.
- **Space-Preserving Palindrome Logic:** In Problem 1, space removal strips single space separators without altering character case. This allows strings with spaced characters to be evaluated cleanly against strict case-sensitive palindrome rules.
- **In-Place Call-Stack Reversal:** In Problem 3, stack reversal operates strictly in-place without instantiating secondary data structures. By leveraging the execution call stack through double recursion (`reverse_stack` and `insert_at_bottom`), elements are unwound and placed at the base, reversing array-based, singly linked, and doubly linked stacks seamlessly without loops.

---

## How to Run

### Problem 2: Smallest Number

Run the script against test input files using standard input redirection:

```bash
python3 smallestNumber.py < Fewest_Resources/fewest_1.txt
```

```bash
python3 smallestNumber.py < Fewest_Resources/fewest_2.txt
```

```bash
python3 smallestNumber.py < Fewest_Resources/fewest_3.txt
```

### Problem 3: Right Triangles

Run the script against test input files using standard input redirection:

```bash
python3 rightTriangles.py < Angles_Resources/rightangles_1.txt
```

```bash
python3 rightTriangles.py < Angles_Resources/rightangles_2.txt```
```

```bash
python3 rightTriangles.py < Angles_Resources/rightangles_3.txt
```
