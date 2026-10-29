# Midterm

## Introduction

This repository contains solutions for the CS526 Midterm. The exam evaluates array prefix analysis, multi-dimensional grid simulations, and matrix-based constraint validation algorithms. The provided Python implementations determine whether any three-day window exceeds half the cumulative seasonal total in a snowfall sequence using prefix differences, simulate daily cellular contagion spread across an $N \times N$ grid until termination, and validate $n \times n$ symbol puzzle boards for row, column, sub-board, and symbol set compliance in $O(n^2)$ time.

---

## Algorithm

### Problem 1: Snowfall

The algorithm converts the cumulative snowfall array into daily snowfall values using prefix differences $D[i] = A[i] - A[i-1]$. It calculates the total snowfall $A[n]$ and evaluates every 3-day sliding window ($D[i] + D[i+1] + D[i+2]$). If any window exceeds half of the total snowfall, it prints `YES`. Otherwise, if no window qualifies or $n < 3$, it prints `NO`.

### Problem 2: Pandemic

The algorithm simulates viral spread across an $N \times N$ grid day by day. In each iteration, healthy counties with two or more orthogonally infected neighbors are identified and updated simultaneously at the end of the day. The simulation runs until a day passes with zero new infections, then checks whether any healthy counties remain.

### Problem 3: Symbol Puzzle Game

The algorithm validates an $n \times n$ board against flexible constraints by verifying symbol sets, rows, columns, and $\sqrt{n} \times \sqrt{n}$ sub-grids in $O(n^2)$ time. It first checks that every non-empty cell contains a symbol from the $n$ allowed values and it determines immediately if an invalid symbol is found. Next, it uses separate hash sets during row and column sweeps to detect duplicate characters while ignoring empty cells (.). Finally, it steps through the matrix in blocks of size $\sqrt{n}$ to ensure each non-overlapping sub-board maintains strict symbol uniqueness. If all cells contain allowed symbols and no row, column, or sub-board contains duplicate symbols, the algorithm outputs `The board is valid`.

---

## Interesting Aspects

- **Prefix-Difference Sliding Window:** In Problem 1, converting cumulative snowfall totals into daily amounts via $D[i] = A[i] - A[i-1]$ enables constant-time $O(1)$ window evaluations, checking all 3-day intervals in a single $O(n)$ pass.
- **Synchronous Grid Propagation:** In Problem 2, separating neighbor counting from state mutation ensures all counties update simultaneously per day without newly infected counties prematurely infecting adjacent neighbors on the same step.
- **Generalized Sub-grid Mapping:** In Problem 3, using integer square root calculations ($k = \sqrt{n}$) allows the exact same $O(n^2)$ validation logic to dynamically scale across various matrix dimensions (such as $4 \times 4$ or $9 \times 9$) without hardcoding dimensions.

---

## How to Run

### Problem 1: Snowfall

Run the script against test input files using standard input redirection:

```bash
python3 snowfall.py < input_files/snowfall_input1.txt
```

```bash
python3 snowfall.py < input_files/snowfall_input2.txt
```

```bash
python3 snowfall.py < input_files/snowfall_input3.txt
```

```bash
python3 snowfall.py < input_files/snowfall_input4.txt
```

### Problem 2: Pandemic

Run the script against test input files using standard input redirection:

```bash
python3 pandemic.py < input_files/pandemic_input1.txt
```

```bash
python3 pandemic.py < input_files/pandemic_input2.txt
```

### Problem 3: Symbol Puzzle Game

Run the script against test input files using standard input redirection:

```bash
python3 puzzle_game.py < input_files/puzzle_game_input1.txt
```

```bash
python3 puzzle_game.py < input_files/puzzle_game_input2.txt
```

```bash
python3 puzzle_game.py < input_files/puzzle_game_input3.txt
```

```bash
python3 puzzle_game.py < input_files/puzzle_game_input4.txt
```
