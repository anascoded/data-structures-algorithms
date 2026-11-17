# Coding Assignment 6

## Introduction

This repository contains solutions for CS526 Homework Assignment 6. The assignment covers priority queues, pointer-based binary min-heaps, and dual-heap streaming algorithms. The implementations merge $k$ sorted checkout logs using a bounded min-priority queue, construct a linked-node binary min-heap with $O(\log n)$ binary-path navigation and ASCII tree visualization, and compute real-time running medians over an unsorted stream of sales using paired min and max heaps.

---

## Algorithm

### Problem 1: Merge Sort

The algorithm merges $k$ sorted register sales logs into a single list of `(time, register)` pairs ordered by sale time, breaking ties in favor of the lower-numbered register. Because each input log is already sorted in non-decreasing order, the globally smallest remaining sale must always be at the front of one of the $k$ logs.

The solution uses a custom binary min-heap (`MinPriorityQueue`) bounded to at most $k$ entries:

- **Initialization:** Iterate through the $k$ logs (indexed $1 \dots k$) and push the first entry of each non-empty log into the priority queue as a 3-tuple `(time, register_number, element_index)`.
- **Extraction & Advancement:** While the priority queue is non-empty, pop the minimum tuple `(time, reg, idx)` and append `(time, reg)` to the merged result. Python’s lexicographical tuple comparison naturally orders by `time` first and breaks ties using the smaller `register_number`. If register `reg` has a subsequent entry at `idx + 1`, push it into the priority queue.

With $N$ total sales across $k$ registers, each push and pop takes $O(\log k)$ time, yielding $O(N \log k)$ total runtime and $O(k)$ auxiliary space.

### Problem 2: Heap

The algorithm implements a binary min-heap (`LinkedMinHeap`) using explicit linked nodes (`HeapNode`), where each node stores its value alongside pointers to its `left` child, `right` child, and `parent`—without storing the heap in an array or list.

To maintain the complete binary tree shape and locate insertion or deletion targets in $O(\log n)$ time, nodes are logically numbered from $1$ in level order:

- **Binary-Path Navigation (`_get_node_at`):** Stripping the leading `1` from the binary representation of a 1-based position `pos` yields the exact path from the root (`0` = left child, `1` = right child). Inserting at size $n$ navigates directly to parent $\lfloor n / 2 \rfloor$, attaches the new leaf, and sifts up while strictly smaller than its parent.
- **Extraction & Arbitrary Deletion:** `extract_min` swaps the root value with the last node at position $n$, detaches that leaf, and sifts down. `delete(value)` locates a matching node (pruning subtrees whose root exceeds `value`), replaces it with node $n$, and sifts either up or down to restore heap order.
- **Bulk Construction & Sorting:** `build(values)` wires a complete linked tree in $O(n)$ time and applies Floyd's bottom-up `sift_down` from position $\lfloor n / 2 \rfloor$ down to $1$. `heap_sort()` clones the linked structure so the original heap remains intact while repeatedly calling `extract_min()`. `print_heap()` calculates tree height and renders nodes with `/` and `\` branch connectors on a 2D character grid.

### Problem 3: Running Median

The algorithm maintains a live running median in $O(\log n)$ time per incoming sale and $O(1)$ query time by partitioning all seen sales across two heaps built directly from Problem 2’s linked-node implementation:

- `lower_half` (`LinkedMaxHeap`, extending `LinkedMinHeap` via value negation) stores the smaller half of the sales, keeping the largest of the small values at its root.
- `upper_half` (`LinkedMinHeap`) stores the larger half of the sales, keeping the smallest of the large values at its root.

After each sale is inserted into the appropriate half, the heaps are rebalanced so two invariants always hold:

1. **Order Invariant:** Every value in `lower_half` is less than or equal to every value in `upper_half` (`lower_half.peek() <= upper_half.peek()`).
2. **Size Balance Invariant:** `len(lower_half)` is either equal to `len(upper_half)` or `len(upper_half) + 1`.

When the total number of sales is odd, the median is immediately `float(lower_half.peek())`; when even, it is `(lower_half.peek() + upper_half.peek()) / 2.0`. Across $n$ sales, total runtime is $O(n \log n)$ and space is $O(n)$.

---

## Interesting Aspects

- **Bounded-Memory $k$-Way Merging:** By pushing only the head of each register log and advancing one pointer per pop, the priority queue never exceeds $k$ elements regardless of how large the individual sales logs grow, while Python tuple ordering handles tie-breaking cleanly without custom comparator wrappers.
- **Pointer-Based Tree Navigation via Bit Paths:** Without array index arithmetic (`2i + 1`), locating the next open slot in a linked complete binary tree would normally require an $O(n)$ level-order scan. Decoding the bits of the 1-based size after the leading `1` restores $O(\log n)$ random access to both the insertion parent and the last leaf node.
- **Zero-Duplication Max-Heap Extension:** Subclassing `LinkedMinHeap` to negate values on insertion and extraction turns the linked min-heap into a max-heap without duplicating any pointer-rewiring or sifting logic, keeping the dual-heap median tracker concise and bug-free.

---

## How to Run

### Problem 1: Merge Sort

Run the script directly to execute the randomized BST operations demonstration:

```bash
python3 merge_sort.py < problem1_res/merge_input1.txt
```

```bash
python3 merge_sort.py < problem1_res/merge_input2.txt
```

```bash
python3 merge_sort.py < problem1_res/merge_input3.txt
```

```bash
python3 merge_sort.py < problem1_res/merge_input4.txt
```

```bash
python3 merge_sort.py < problem1_res/merge_input5.txt
```

```bash
python3 merge_sort.py < problem1_res/merge_input6.txt
```

```bash
python3 merge_sort.py < problem1_res/merge_input7.txt
```

```bash
python3 merge_sort.py < problem1_res/merge_input8.txt
```

```bash
python3 merge_sort.py < problem1_res/merge_input9.txt
```

### Problem 2: Heap

Run the script against test input files:

```bash
python3 heap.py < problem2_res/heap_input1.txt
```

```bash
python3 heap.py < problem2_res/heap_input2.txt
```

```bash
python3 heap.py < problem2_res/heap_input3.txt
```

```bash
python3 heap.py < problem2_res/heap_input4.txt
```

```bash
python3 heap.py < problem2_res/heap_input5.txt
```

```bash
python3 heap.py < problem2_res/heap_input6.txt
```

```bash
python3 heap.py < problem2_res/heap_input7.txt
```

```bash
python3 heap.py < problem2_res/heap_input8.txt
```

```bash
python3 heap.py < problem2_res/heap_input9.txt
```

```bash
python3 heap.py < problem2_res/heap_input10.txt
```

### Problem 3: Running Median

Run the script against test input files:

```bash
python3 median.py < problem3_res/median_input1.txt
```

```bash
python3 median.py < problem3_res/median_input2.txt
```

```bash
python3 median.py < problem3_res/median_input3.txt
```

```bash
python3 median.py < problem3_res/median_input4.txt
```

```bash
python3 median.py < problem3_res/median_input5.txt
```

```bash
python3 median.py < problem3_res/median_input6.txt
```

```bash
python3 median.py < problem3_res/median_input7.txt
```

```bash
python3 median.py < problem3_res/median_input8.txt
```

```bash
python3 median.py < problem3_res/median_input9.txt
```

```bash
python3 median.py < problem3_res/median_input10.txt
```

```bash
python3 median.py < problem3_res/median_input11.txt
```
