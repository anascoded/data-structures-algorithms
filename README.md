# Coding Assignment 4

## Introduction

This repository contains solutions for CS526 Homework Assignment 4. The assignment explores tree traversal algorithms, greedy optimization strategies, and geometry vector techniques. The provided implementations explain preorder, breadth-first, postorder, and in-order traversals on general and binary trees, determine the minimum subset of array elements whose sum exceeds a target value using a greedy approach, and compute the number of unique right-angled triangles formed by a set of 2D coordinates using exact vector slope and $90^\circ$ direction analysis.

---

## Algorithm

### Problem 1: A

Preorder Tree Traversal (Root $\rightarrow$ Children): (`A, B, E, H, F, I, C, D, G`)

- Preorder traversal visits the root first, followed recursively by its children from left to right.

Breadth-First Tree Traversal (Level by Level): (`A, B, C, D, E, F, G, H, I`)

- Breadth-first traversal processes the tree level by level using a queue, visiting all nodes at the current depth before moving to the next level.

Postorder Tree Traversal (Children $\rightarrow$ Root): (`H, E, I, F, B, C, G, D, A`)

- Postorder traversal recursively processes all subtrees left-to-right before visiting their parent root node.

### Problem 1: B

In-Order Tree Traversal (Left $\rightarrow$ Root $\rightarrow$ Right): (`D, G, B, E, A, C, H, F, I`)

- The algorithm performs an in-order traversal on a binary tree by recursively exploring the left subtree, visiting the current node, and then recursively exploring the right subtree.

### Problem 2: Smallest Number

The algorithm finds the minimum number of array elements whose sum strictly exceeds target $T$. It sorts the array in descending order so that the largest values are selected first. It then iterates through the sorted array, maintaining a running total and element count until the total exceeds $T$, to make sure we have an optimal minimum element count.

### Problem 3: Right Triangles

The algorithm computes the total number of right triangles in $O(n^2)$ time by evaluating each point as a potential $90^\circ$ vertex as the professor hinted in class. For a fixed vertex $P_i$, it calculates normalized direction vectors $(dx, dy)$ for all other points using integer greatest common divisors ($\gcd$). It then counts occurrences of perpendicular vectors $(-dy, dx)$ corresponding to $90^\circ$ counter-clockwise rotations, multiplying directional ray counts to determine all right triangles anchored at $P_i$.

---

## Interesting Aspects

- **Greedy Optimality Guarantee:** In Problem 2, picking the largest available elements first strictly minimizes the number of elements required to exceed target $T$, reducing what could be a complex subset-sum problem down to an efficient $O(n \log n)$ sort.
- **$O(n^2)$ Perpendicular Vector Matching:** In Problem 3, counting perpendicular direction vectors around each anchor point reduces the search complexity from an $O(n^3)$ triplet check to an $O(n^2)$ frequency lookup, processing 1,000 points in just 0.76 seconds (tested with the command `time`).
- **Exact Vector Normalization:** Problem 3 avoids floating-point division errors when calculating slopes by reducing direction vectors using `math.gcd(dx, dy)`, ensuring precise $90^\circ$ orientation matching without precision loss.

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
python3 rightTriangles.py < Angles_Resources/rightangles_2.txt
```

```bash
python3 rightTriangles.py < Angles_Resources/rightangles_3.txt
```
