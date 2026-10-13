# Assignment 3 - Problem 1
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-10-12

import sys

# Replace single spaces in a string with no spaces and checks if the string is a palindrome
def is_palindrome(s):
    """
    Determines whether a string is a palindrome.
    """
    # Remove single spaces while maintaining case sensitivity
    cleaned = s.replace(" ", "")
    return cleaned == cleaned[::-1]


# main function to read input and check for palindromes
def main():
    count = 0
    for line in sys.stdin:
        line = line.rstrip("\r\n")
        if not line:
            continue
        
        result = is_palindrome(line)
        print(result)
        if result:
            count += 1
            
    print(count)

# Entry point for the script
if __name__ == "__main__":
    main()