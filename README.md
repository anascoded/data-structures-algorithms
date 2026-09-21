# Coding Assignment 1

## Steps to approach the solution

- Step 1: The program asks the user to enter a filename. For example, the user might enter something like **"file.txt"**.
  
- Step 2: The program checks whether the file is a .txt file. We use ***.lower()*** to convert the filename to lowercase, and ***.endswith(".txt")*** to check whether the filename ends with **.txt**
  
- Step 3: If the file is not a text file, it prints an error message.
  
- Step 4: If the file type is correct, the program checks whether the file actually exists. If not, it prints **"File not found."**
  
- Step 5: If the file exists and is a **.txt** file, the program opens it, reads the file one line at a time, and prints it. We use ***strip()*** to remove the newline character and extra spaces from the beginning and end of the line.

