# CS526 Homework Assignment 2

## Introduction

This repository contains solutions for CS526 Homework Assignment 2. The assignment explores the advantages of linked list optimizations, the implementation of custom singly and doubly linked list data structures with robust driver parsers, dynamic recursive problem solving, and error-tolerant stream processing. The provided Python modules implement a complete Singly Linked List with head/tail references, a recursive climbing stairs sequence and path visualizer, and a Sorted Doubly Linked List supporting advanced statistical operations and early-stopping recursive traversals.

---

## Algorithm

### Problem 1: Tail Pointer Advantage

A tail pointer maintains a direct reference to the final node in a linked list structure. In a standard singly linked list without a tail reference, appending a new node requires traversing all $n$ nodes from the head to reach the terminus, resulting in a time complexity of $O(n)$. By maintaining a tail reference alongside the head, inserting an element at the end (`append`) is optimized to an $O(1)$ constant time operation. The algorithm directly updates `tail.next` to point to the newly instantiated node and subsequently reassigns the `tail` pointer to this new node.
Without a tail pointer, appending a new node requires traversing the entire list from the head node to the end, which takes O(n) time complexity.

### Problem 2: Singly Linked List (CRUD Operations)

The `SinglyLinkedList` class maintains `head`, `tail`, and `_size` properties to manage node sequences efficiently. Insertion and deletion algorithms adjust pointers conditionally depending on whether operations target boundary nodes (head or tail) or internal positions. Operations, like `get(index)` and `update(index, value)`, iterate sequentially through node references up to the target index, if bounds are violated an `IndexError` is raised. The `delete(value)` method updates `tail` pointer dynamically whenever the last element is removed.

### Problem 3: Climbing Stairs (Recursive Combinations)

This algorithm uses recursion to evaluate pathways for reaching target step $n$ using step increments of 1, 2, or 3. The recursive helper `get_combinations(n, path)` branches into three sub-problems—`n - 1`, `n - 2`, and `n - 3`—appending the chosen step to the current path vector. Base cases return `[path]` when $n = 0$ (a valid path completion) or an empty list when $n < 0$ (an invalid overshoot). The aggregate combinations are combined across branches without employing explicit loops, matching mathematical recurrence while constructing all valid step sequences.

### Problem 4: Sorted Doubly Linked List

The `SortedDoublyLinkedList` maintains elements in ascending order by performing linear insertions (`add`) that position new nodes immediately before the first node with a larger value. Recursive helper functions facilitate sequence traversals like `total()`, `count(value)`, and `exists(value)`. Because the list is ordered, searching and counting algorithms implement early stopping: recursion terminates as soon as a node value exceeds the query target ($node.value > value$). Statistical methods (`median` and `sum_middle_three`) navigate directly to center indices derived from list size calculation ($n // 2$), evaluating odd versus even structural offsets to compute central sums or medians.

---

## Interesting Aspects

- **Early-Stopping Optimization in Sorted Lists:** In Problem 4, recursive search algorithms (`exists` and `count`) leverage the sorted invariant of the doubly linked list. Traversal halts immediately when `node.value > target`, avoiding full $O(n)$ list scans on missing or larger elements.
- **Format-Preserving Numeric Parsers:** Both driver programs (`problem2_driver.py` and `problem4_driver.py`) handle mixed input types cleanly by attempting integer and float conversions before falling back to string processing, ensuring output strings retain exact formatting matches.
- **Unified Boundary Management:** Node insertions and removals in both singly and doubly linked lists carefully handle single-element lists, ensuring `head` and `tail` references are correctly set to `None` when the list becomes empty.
- **Pure Recursive Execution:** The stair climbing path generator adheres strictly to functional recursion without local loops, building combination trees purely via recursive list concatenations.

---

## How to Run

### Problem 1

A tail pointer is usually used to maintain efficient access to the end of the list, simplifying append operations and ensuring proper list structure.

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
