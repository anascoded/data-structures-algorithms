# Assignment 3 - Problem 2
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-10-12

import sys

# Get all unique substrings of a string s using recursion
def get_substrings_recursive(s, start=0, end=1, found_set=None):
    """
    Recursively finds all unique substrings of a string s.
    """
    if found_set is None:
        found_set = set()

    n = len(s) # Length of the string
    if start >= n:
        return found_set

    if end <= n:
        found_set.add(s[start:end])
        return get_substrings_recursive(s, start, end + 1, found_set)
    else:
        return get_substrings_recursive(s, start + 1, start + 2, found_set)


# main function to read input and output unique substrings
def main():
    input_text = sys.stdin.read().strip()
    if not input_text:
        return

    # Extract the first line of input
    first_line = input_text.splitlines()[0]
    
    unique_subs = get_substrings_recursive(first_line)
    
    # Sort lexicographically and output
    sorted_subs = sorted(list(unique_subs))
    for sub in sorted_subs:
        print(sub)
        
    print(len(sorted_subs))

# Entry point for the script
if __name__ == "__main__":
    main()