# Midterm - Problem 3
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-10-28

import sys
import math

# Function to validate the symbol puzzle board
def solve(filepath_or_stream):
    if isinstance(filepath_or_stream, str):
        with open(filepath_or_stream, 'r') as f:
            lines = f.read().splitlines()
    else:
        lines = filepath_or_stream.read().splitlines()

    lines = [l.strip() for l in lines if l.strip()]
    if not lines:
        return

    # Parse input
    n = int(lines[0])
    allowed_symbols = set(lines[1].split(','))
    k = int(math.isqrt(n))

    # Validate the board
    board = []
    for i in range(2, 2 + n):
        board.append(lines[i].split(','))

    # Check 1: Allowed Symbols
    for r in range(n):
        for c in range(n):
            val = board[r][c]
            if val != '.' and val not in allowed_symbols:
                print("The board is invalid")
                return

    # Check 2: Row Uniqueness
    for r in range(n):
        seen = set()
        for c in range(n):
            val = board[r][c]
            if val != '.':
                if val in seen:
                    print("The board is invalid")
                    return
                seen.add(val)

    # Check 3: Column Uniqueness
    for c in range(n):
        seen = set()
        for r in range(n):
            val = board[r][c]
            if val != '.':
                if val in seen:
                    print("The board is invalid")
                    return
                seen.add(val)

    # Check 4: Sub-board (k x k) Uniqueness
    for br in range(0, n, k):
        for bc in range(0, n, k):
            seen = set()
            for r in range(br, br + k):
                for c in range(bc, bc + k):
                    val = board[r][c]
                    if val != '.':
                        if val in seen:
                            print("The board is invalid")
                            return
                        seen.add(val)

    print("The board is valid")

# Entry point for the script
if __name__ == "__main__":
    if len(sys.argv) > 1:
        solve(sys.argv[1])
    else:
        solve(sys.stdin)
