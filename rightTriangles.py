# Assignment 4 - Problem 3
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-10-19

import sys
import math
from collections import Counter

# Function to normalize direction vectors and count right triangles formed by given points
def canonical_dir(dx, dy):
    """Normalize direction vector to its reduced primitive form."""
    g = math.gcd(dx, dy)
    dx //= g
    dy //= g
    return (dx, dy)

# Function to count the number of right triangles formed by a set of points
def count_right_triangles(points):
    n = len(points)
    total_right_triangles = 0

    # Iterate through each point as the vertex holding the 90-degree angle
    for i in range(n):
        x1, y1 = points[i]
        angle_counts = Counter()

        for j in range(n):
            if i == j:
                continue
            dx = points[j][0] - x1
            dy = points[j][1] - y1
            
            # Reduce vector to primitive direction
            c_dir = canonical_dir(dx, dy)
            angle_counts[c_dir] += 1

        # Check for perpendicular vectors (90-degree rotated rays)
        for (dx, dy), count in angle_counts.items():
            # A 90 degree counter-clockwise rotation of (dx, dy) is (-dy, dx)
            perp_dir = canonical_dir(-dy, dx)
            if perp_dir in angle_counts:
                total_right_triangles += count * angle_counts[perp_dir]

    return total_right_triangles

# Main function to read input and count right triangles
def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    lines = [line.strip() for line in lines if line.strip()]
    if not lines:
        return

    num_points = int(lines[0])
    points = []
    for line in lines[1:num_points + 1]:
        parts = line.split()
        points.append((int(parts[0]), int(parts[1])))

    ans = count_right_triangles(points)
    print(f"The number of right triangles is: {ans}")

# Entry point for the script
if __name__ == "__main__":
    main()