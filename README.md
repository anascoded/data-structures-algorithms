# Data Structures and Algorithms

This repository contains my assignments and solutions for **CS527: Data Structures and Algorithms**.
# Coding Assignment 3

## Introduction

This repository contains solutions for CS526 Homework Assignment 3.

---

## Algorithm

### Problem 1: Palindrome

A tail pointer maintains a direct reference to the final node in a linked list structure. In a standard singly linked list without a tail reference, appending a new node requires traversing all $n$ nodes from the head to reach the terminus, resulting in a time complexity of $O(n)$. By maintaining a tail reference alongside the head, inserting an element at the end (`append`) is optimized to an $O(1)$ constant time operation.

### Problem 2: Substrings

The `SinglyLinkedList` class maintains `head`, `tail`, and `_size` properties to manage node sequences efficiently. Insertion and deletion algorithms adjust pointers conditionally depending on whether operations target boundary nodes (head or tail) or internal positions. Operations, like `get(index)` and `update(index, value)`, iterate through node references up to the target index, if bounds are violated an `IndexError` is raised. The `delete(value)` method updates `tail` pointer dynamically whenever the last element is removed.

### Problem 3: Climbing Stairs (Recursive Combinations)

This algorithm uses recursion to evaluate pathways for reaching target step $n$ using step increments of 1, 2, or 3. The recursive helper `get_combinations(n, path)` branches into three sub-problems `n - 1`, `n - 2`, and `n - 3` appending the chosen step to the current path vector. The base cases return `[path]` when $n = 0$ or an empty list when $n < 0$ (an invalid overshoot).

### Problem 4: Sorted Doubly Linked List

The `SortedDoublyLinkedList` maintains elements in ascending order by performing linear insertions (`add`) that position new nodes immediately before the first node with a larger value. Recursive helper functions facilitate sequence traversals like `total()`, `count(value)`, and `exists(value)`. Because the list is ordered, searching and counting algorithms implement early stopping: recursion terminates as soon as a node value exceeds the query target ($node.value > value$). Methods (`median` and `sum_middle_three`) go directly to center indices that they get from list size calculation, and evaluate odd versus even structural offsets to compute central sums or medians.

---

## Interesting Aspects

- **Early-Stopping Optimization in Sorted Lists:** In Problem 4, recursive search algorithms (`exists` and `count`) leverage the sorted invariant of the doubly linked list. Traversal stops immediately when `node.value > target`, avoiding full $O(n)$ list scans on missing or larger elements.
- **Format-Preserving Numeric Parsers:** Both driver programs (`problem2_driver.py` and `problem4_driver.py`) handle mixed input types cleanly by attempting integer and float conversions before falling back to string processing, ensuring output strings retain exact formatting matches.
- **Unified Boundary Management:** Node insertions and removals in both singly and doubly linked lists carefully handle single-element lists, ensuring `head` and `tail` references are correctly set to `None` when the list becomes empty.

---

## How to Run

### Problem 2: Singly Linked List

Run the driver against test input files using standard input redirection:

```bash
python3 problem2_driver.py < problem2Resources/problem2_basic.txt
```

```bash
python3 problem2_driver.py < problem2Resources/problem2_create.txt
```

```bash
python3 problem2_driver.py < problem2Resources/problem2_errors.txt
```

```bash
python3 problem2_driver.py < problem2Resources/problem2_delete.txt
```

```bash
python3 problem2_driver.py < problem2Resources/problem2_update.txt
```

```bash
python3 problem2_driver.py < problem2Resources/problem2_read.txt
```

```bash
python3 problem2_driver.py < problem2Resources/problem2_update.txt
```

### Problem 3: Climbing Stairs

Execute the recursive combination script directly:

```bash
python3 problem3.py
```

### Problem 4: Sorted Doubly Linked List

Run the driver against any of the resource test scripts:

```bash
python3 problem4_driver.py < problem4Resources/problem4_basic.txt
```

```bash
python3 problem4_driver.py < problem4Resources/problem4_duplicates.txt
```

```bash
python3 problem4_driver.py < problem4Resources/problem4_errors.txt
```

```bash
python3 problem4_driver.py < problem4Resources/problem4_example.txt
```

```bash
python3 problem4_driver.py < problem4Resources/problem4_mixed.txt
```

```bash
python3 problem4_driver.py < problem4Resources/problem4_numbers.txt
```

```bash
python3 problem4_driver.py < problem4Resources/problem4_positions.txt
```

```bash
python3 problem4_driver.py < problem4Resources/problem4_simple.txt
```

```bash
python3 problem4_driver.py < problem4Resources/problem4_statistics.txt
```

## Repository Structure

Each assignment is organized in its own Git branch. The `main` branch contains the general repository information, while each assignment branch contains the corresponding assignment solution.

| Branch         | Description  |
| -------------- | ------------ |
| `assignment-1` | Assignment 1 |
| `assignment-2` | Assignment 2 |
| `assignment-3` | Assignment 3 |
| `assignment-4` | Assignment 4 |
| `assignment-5` | Assignment 5 |
| `assignment-6` | Assignment 6 |
| `assignment-7` | Assignment 7 |

> The branch list will be updated as new assignments are completed.

## Course Information

* **Course:** CS527 – Data Structures and Algorithms
* **Program:** M.S. in Software Development
* **University:** Boston University

## Assignments

To view the solution for a specific assignment, switch to the corresponding branch:

```bash
git switch assignment-1
```

Replace `assignment-1` with the branch for the assignment you want to view.

## Technologies

All assignments use **Python** as the main programming languages and tools depending on each assignment's requirements.

## Disclaimer

These solutions are provided for educational and reference purposes.
