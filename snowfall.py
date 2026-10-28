# Midterm - Problem 1
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-10-28

import sys

# Function to simulate the spread of a pandemic in a grid of counties
def solve(filepath_or_stream):
    if isinstance(filepath_or_stream, str):
        with open(filepath_or_stream, 'r') as f:
            lines = f.read().splitlines()
    else:
        lines = filepath_or_stream.read().splitlines()

    # Parse input
    lines = [l.strip() for l in lines if l.strip()]
    if not lines:
        return

    # Parse the number of days and the snowfall amounts
    n = int(lines[0])
    A = list(map(int, lines[1].split()))

    # Check if there are at least 3 days of snowfall
    if n < 3:
        print(f"{' '.join(map(str, A))} solution: NO")
        return

    # Calculate total snowfall and half of it
    total_snowfall = A[-1]
    half_total = total_snowfall / 2.0

    # Check for any 3-day period where the snowfall exceeds half of the total
    found = False
    for i in range(n - 2):
        prev = A[i - 1] if i > 0 else 0
        three_day_sum = A[i + 2] - prev
        if three_day_sum > half_total:
            found = True
            break

    # Output the result
    result = "YES" if found else "NO"
    print(f"{' '.join(map(str, A))} solution: {result}")

# Entry point for the script
if __name__ == "__main__":
    if len(sys.argv) > 1:
        solve(sys.argv[1])
    else:
        solve(sys.stdin)