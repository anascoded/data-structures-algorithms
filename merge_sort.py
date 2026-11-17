# Assignment 6 - Problem 1
# Name: Anas S.
# Course: CS526 - Data Structures and Algorithms
# Date: 2026-11-16

import ast
import sys

# Class MinPriorityQueue implements a bounded-memory min-heap for merging k sorted logs.
class MinPriorityQueue:
    """Array-backed binary min-heap restricted to at most k entries."""

    # Initialize an empty priority queue.
    def __init__(self):
        self._data = []

    # Return the number of elements in the priority queue.
    def __len__(self):
        return len(self._data)

    # Return True if the priority queue is empty, False otherwise.
    def push(self, item):
        self._data.append(item)
        self._sift_up(len(self._data) - 1)

    # Pop the root of the min-heap and return it, maintaining the heap property.
    def pop(self):
        if not self._data:
            raise IndexError("pop from empty priority queue")
        if len(self._data) == 1:
            return self._data.pop()

        root = self._data[0]
        self._data[0] = self._data.pop()
        self._sift_down(0)
        return root

    # Sift up to maintain the min-heap property after insertion
    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            # If the current node is smaller than its parent, swap them and continue sifting up
            if self._data[idx] < self._data[parent]:
                self._data[idx], self._data[parent] = (
                    self._data[parent],
                    self._data[idx],
                )
                idx = parent
            else:
                break

    # Sift down to maintain the min-heap property after popping the root
    def _sift_down(self, idx):
        n = len(self._data)
        while True:
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            # Check if left child exists and is smaller than current smallest
            if left < n and self._data[left] < self._data[smallest]:
                smallest = left

            # Check if right child exists and is smaller than current smallest
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right

            # If the smallest is not the current index, swap and continue sifting down
            if smallest != idx:
                self._data[idx], self._data[smallest] = (
                    self._data[smallest],
                    self._data[idx],
                )
                idx = smallest
            else:
                break

# Entry point for the merge_k_logs demonstration
def merge_k_logs(logs):
    pq = MinPriorityQueue()

    # Seed the priority queue with at most one entry per register
    for reg_idx, log in enumerate(logs, start=1):
        if log:
            # Tuple order ensures sorting by time, then lower register number
            pq.push((log[0], reg_idx, 0))

    merged = []
    while len(pq) > 0:
        time_val, reg_num, elem_idx = pq.pop()
        merged.append((time_val, reg_num))

        next_idx = elem_idx + 1
        register_log = logs[reg_num - 1]
        if next_idx < len(register_log):
            pq.push((register_log[next_idx], reg_num, next_idx))

    return merged

# Main function to process input files and print results.
def main():
    logs = []
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            logs.append(ast.literal_eval(stripped))

    result = merge_k_logs(logs)
    print(result)

# Entry point for the script.
if __name__ == "__main__":
    main()