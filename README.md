# Coding Assignment 1

## Introduction


- I have taken many programming classes over 10+ years of college-level courses using different programming languages. CS526 is my 7th programming course here at BU, but overall I've taken 20+ programming courses.

- I know both Java and Python, but I've done more programming in Java than Python.

- I'm in my second (and last) year of the MS in Software Development program.

- I've taken a similar course in my undergrad at UMass using Java. I also used the same concepts in other classes.


## Steps to approach the solution

- Step 1: The user runs the program from the file directory using the command **python3 main.py**.

- Step 2: The program asks the user to enter a filename. For example, the user might enter something like **"file.txt"**.
  
- Step 3: The program checks whether the file is a .txt file. We use ***.lower()*** to convert the filename to lowercase, and ***.endswith(".txt")*** to check whether the filename ends with **.txt**
  
- Step 4: If the file is not a text file, it prints an error message.
  
- Step 5: If the file type is correct, the program checks whether the file actually exists. If not, it prints **"File not found."**
  
- Step 6: If the file exists and is a **.txt** file, the program opens it, reads the file one line at a time, and prints it. We use ***strip()*** to remove the newline character and extra spaces from the beginning and end of the line.


