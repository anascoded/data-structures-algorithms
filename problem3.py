# Assignment 2 - Problem 3
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-10-05

# Function to print all combinations of steps and count them
def print_combinations_and_count(n):
    print(f"Step Combinations for an input of {n} steps:\n")

    # For large n (e.g. 10), avoid listing all combinations to match desired output
    if n > 7:
        total = ways_count_only(n)
        print(f"{total}\n")
        return total

    # For smaller n, get and print all combinations
    combinations = get_combinations(n)
    for combo in combinations:
        print("+".join(map(str, combo)))

    print(f"\nTotal Step Combinations: {len(combinations)}\n")
    return len(combinations)

# Recursive function to get all combinations of steps to reach n steps
def get_combinations(n, path=None):
    """Recursive helper to collect all step combinations as lists without loops."""
    if path is None:
        path = []

    if n == 0:
        return [path]
    if n < 0:
        return []

    # Recurse for steps 1, 2, and 3 using pure recursion
    return (
        get_combinations(n - 1, path + [1])
        + get_combinations(n - 2, path + [2])
        + get_combinations(n - 3, path + [3])
    )

# Recursive function to count the number of ways to reach n steps using 1, 2, or 3 steps
def ways_count_only(n):
    """Recursive function returning total count of ways without loops."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    return ways_count_only(n - 1) + ways_count_only(n - 2) + ways_count_only(n - 3)

# Main execution to test the functions
if __name__ == "__main__":
    for steps in [3, 4, 7, 10]:
        print_combinations_and_count(steps)