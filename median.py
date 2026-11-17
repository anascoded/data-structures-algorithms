# Assignment 6 - Problem 3
# Name: Anas S.
# Course: CS526 - Data Structures and Algorithms
# Date: 2026-11-16

import ast
import sys
from heap import LinkedMinHeap

# Class LinkedMaxHeap extends LinkedMinHeap to behave as a Max-Heap by storing negated values.
class LinkedMaxHeap(LinkedMinHeap):

    # Override insert to store negated values
    def insert(self, value):
        super().insert(-value)

    # Override peek to return the negated value of the root
    def peek(self):
        return -super().peek()

    # Override extract_min to call extract_min from the parent class
    def extract_min(self):
        return -super().extract_min()

    # Override extract_max to call extract_min from the parent class
    def extract_max(self):
        return self.extract_min()


def running_medians(sales):
    if not sales:
        return []

    lower_half = LinkedMaxHeap()  # Stores smaller half of sales (max at root)
    upper_half = LinkedMinHeap()  # Stores larger half of sales (min at root)
    medians = []

    for sale in sales:
        # 1. Place new sale into the appropriate half
        if lower_half.is_empty() or sale <= lower_half.peek():
            lower_half.insert(sale)
        else:
            upper_half.insert(sale)

        # 2. Rebalance so size invariant holds:
        if len(lower_half) > len(upper_half) + 1:
            upper_half.insert(lower_half.extract_max())
        elif len(upper_half) > len(lower_half):
            lower_half.insert(upper_half.extract_min())

        # 3. Compute median in O(1) time
        if len(lower_half) > len(upper_half):
            medians.append(float(lower_half.peek()))
        else:
            medians.append((lower_half.peek() + upper_half.peek()) / 2.0)

    return medians

# Main function to process input files and print results.
def main():
    raw = sys.stdin.read().strip()
    if not raw:
        print([])
        return
    sales = ast.literal_eval(raw)
    print(running_medians(sales))

# Entry point for the script.
if __name__ == "__main__":
    main()