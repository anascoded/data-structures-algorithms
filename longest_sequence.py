# Assignment 5 - Problem 3
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-11-09

import os
import sys
import glob
import re

# Find the longest alternating increasing sequence from A and B.
def longest_sequence(A, B):
    n, m = len(A), len(B)
    fa, fb = [1] * n, [1] * m
    pa, pb = [None] * n, [None] * m

    # Process positions in increasing order
    for p in range(max(n, m)):
        if p < n:
            for j in range(min(p, m)):
                if B[j] < A[p] and fb[j] + 1 > fa[p]:
                    fa[p], pa[p] = fb[j] + 1, ("B", j)
        if p < m:
            for i in range(min(p, n)):
                if A[i] < B[p] and fa[i] + 1 > fb[p]:
                    fb[p], pb[p] = fa[i] + 1, ("A", i)

    # Find the longest sequence and its ending position.
    best, end = 0, None
    for i in range(n):
        if fa[i] > best:
            best, end = fa[i], ("A", i)
    for j in range(m):
        if fb[j] > best:
            best, end = fb[j], ("B", j)
    if end is None:
        return 0, []

    # Reconstruct the sequence from the predecessor pointers.
    seq = []
    while end:
        which, idx = end
        seq.append((A if which == "A" else B)[idx])
        end = (pa if which == "A" else pb)[idx]
    return best, seq[::-1]

# Read the input file and return the two sequences A and B.
def read_input(path):
    with open(path) as f:
        nums = list(map(int, f.read().split()))
    n, m = nums[0], nums[1]
    return nums[2:2 + n], nums[2 + n:2 + n + m]

# Main function to process input files and print results.
def main():
    show = "--show" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--show"]
    files = args or sorted(
        glob.glob("longest_seq*.txt"),
        key=lambda p: int(re.findall(r"\d+", p)[-1]))
    for path in files:
        length, seq = longest_sequence(*read_input(path))
        print(f"File Input: {os.path.basename(path)}")
        print(f"Longest Sequence: {length}")
        if show:
            print(f"  One optimal sequence: {seq}")

# Entry point for the script.
if __name__ == "__main__":
    main()