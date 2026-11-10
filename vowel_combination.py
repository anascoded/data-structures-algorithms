# Assignment 5 - Problem 2
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-11-09

import os
import sys
import glob
import re

# Morse codes for vowels
VOWELS = {"A": ".-", "E": ".", "I": "..", "O": "---", "U": "..-"}

# Count the number of vowel-only Morse decodings.
def count_vowel_sequences(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for code in VOWELS.values():
            L = len(code)
            if i >= L and s[i - L:i] == code:
                dp[i] += dp[i - L]
    return dp[n]


# Read the input file and return the Morse sequence.
def read_sequence(path):
    with open(path) as f:
        text = f.read()
    return "".join(re.findall(r"[.\-]", text))  # Keep only dots and dashes

# Main function to process input files and print results.
def main():
    files = sys.argv[1:] or sorted(
        glob.glob("vowel_input*.txt"),
        key=lambda p: int(re.findall(r"\d+", p)[-1]))
    for path in files:
        print(f"File Input: {os.path.basename(path)}")
        print(f"The Number of Vowel combinations is:  {count_vowel_sequences(read_sequence(path))}")

# Entry point for the script.
if __name__ == "__main__":
    main()