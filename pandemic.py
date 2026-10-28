# Midterm - Problem 2
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

    lines = [l.strip() for l in lines if l.strip()]
    if not lines:
        return

    # Parse input
    N = int(lines[0])
    grid = [[False] * N for _ in range(N)]

    # Parse the initially infected counties
    for line in lines[1:]:
        r, c = map(int, line.split())
        grid[r][c] = True

    # Directions for adjacent counties (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Simulate the spread of the pandemic
    while True:
        newly_infected = []
        for r in range(N):
            for c in range(N):
                if not grid[r][c]:
                    infected_neighbors = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc]:
                            infected_neighbors += 1
                    if infected_neighbors >= 2:
                        newly_infected.append((r, c))
        
        # If no new infections occurred, break the loop
        if not newly_infected:
            break

        # Update the grid with newly infected counties
        for r, c in newly_infected:
            grid[r][c] = True

    # Count the number of healthy counties left
    healthy_count = sum(row.count(False) for row in grid)
    if healthy_count > 0:
        print("There are healthy counties left")
    else:
        print("There are no healthy counties left")

# Entry point for the script
if __name__ == "__main__":
    if len(sys.argv) > 1:
        solve(sys.argv[1])
    else:
        solve(sys.stdin)
