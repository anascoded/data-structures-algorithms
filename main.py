# Assignment 1
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-09-14

#
import sys
import os

# Prompt user to enter filename
filename = input("Enter the filename: ")

# Case when file type is not supported
if not filename.lower().endswith(".txt"):
    print("File type is not supported. Please use a txt file.")
    sys.exit(1)

# Case when file is not found
if not os.path.isfile(filename):
    print("File not found.")
    sys.exit(1)

# Open file and print its content line by line
with open(filename, "r") as file:
    for line in file:
        print(line.strip())