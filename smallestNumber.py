# Assignment 4 - Problem 2
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-10-19

import sys

# Function to find the smallest number of elements from an array that sum to a value greater than a target
def main():
    raw_input = sys.stdin.read().splitlines()
    if not raw_input:
        return

    lines = [line.strip() for line in raw_input if line.strip()]
    if len(lines) < 3:
        return

    n = int(lines[0])
    target = int(lines[1])
    array = [int(x) for x in lines[2].split()]

    # Sort descending to take largest elements first
    sorted_array = sorted(array, reverse=True)

    running_sum = 0
    count = 0
    for num in sorted_array:
        running_sum += num
        count += 1
        if running_sum > target:
           break
    # Array and target output for verification
    print("Input: ")
    elements_per_line = 24 # Print array elements in groups of 24
    for i in range(0, len(array), elements_per_line):
        print(",".join(map(str, array[i:i + elements_per_line])))

    print(f"Target: {target} Answer: {count}")

# Entry point for the script
if __name__ == "__main__":
    main()