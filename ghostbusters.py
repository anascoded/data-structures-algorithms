# Assignment 3 - Problem 4
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-10-12

import sys

# Check if two direction vectors are parallel using integer cross product
def are_parallel(dx1, dy1, dx2, dy2):
    """Check if two direction vectors are parallel using integer cross product."""
    return (dx1 * dy2 - dy1 * dx2) == 0

# Check if point p2 lies on the line passing through p1 with direction dir1
def are_collinear(p1, dir1, p2):
    """Check if point p2 lies on the line passing through p1 with direction dir1."""
    x1, y1 = p1
    dx1, dy1 = dir1
    x2, y2 = p2
    return ((x2 - x1) * dy1 - (y2 - y1) * dx1) == 0

# Determine if all ghost streams are parallel and no two streams lie on the same line
def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    # Parse total pairs count n
    n_str = lines[0].strip()
    if not n_str:
        return
    n = int(n_str)

    streams = []
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        
        tokens = line.split()
        if len(tokens) < 6:
            continue

        # Format: B <x> <y> G <x> <y>
        # Index:  0  1   2   3  4   5
        bx, by = int(tokens[1]), int(tokens[2])
        gx, gy = int(tokens[4]), int(tokens[5])
        
        dx = gx - bx
        dy = gy - by
        streams.append(((bx, by), (dx, dy)))

    # Check if the number of streams matches n and n is not zero
    if len(streams) != n or n == 0:
        print("All Ghosts: were not eliminated")
        return

    # All streams must be parallel and no two streams can lie on the same line
    base_p, base_dir = streams[0]
    dx1, dy1 = base_dir

    for i in range(1, n):
        curr_p, curr_dir = streams[i]
        dx2, dy2 = curr_dir

        # Streams must be parallel
        if not are_parallel(dx1, dy1, dx2, dy2):
            print("All Ghosts: were not eliminated")
            return

        # Streams must not lie on the exact same line
        if are_collinear(base_p, base_dir, curr_p):
            print("All Ghosts: were not eliminated")
            return

    print("All Ghosts: were eliminated")


if __name__ == "__main__":
    solve()