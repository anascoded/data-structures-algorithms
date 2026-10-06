# Assignment 2 - Problem 4
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-10-05

import sys
from problem4 import SortedDoublyLinkedList


def parse_number(val_str, line_content):
    """Parse integer or float values."""
    try:
        val = float(val_str)
        return int(val) if val.is_integer() else val
    except ValueError:
        raise ValueError(f"value must be a number, got '{line_content}'")


def format_val(val):
    """Format numeric values consistently for output."""
    if isinstance(val, float) and val.is_integer():
        return str(int(val))
    return str(val)


def main():
    sdll = SortedDoublyLinkedList()

    for line_num, line in enumerate(sys.stdin, 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        tokens = line.split()
        cmd = tokens[0]
        args = tokens[1:]

        try:
            if cmd == "add":
                if len(args) != 1:
                    print(f"line {line_num}: expected 'add <value>', got '{line}'")
                    continue
                val = parse_number(args[0], line)
                sdll.add(val)
                print(f"add({format_val(val)})")

            elif cmd == "delete":
                if len(args) != 1:
                    print(f"line {line_num}: expected 'delete <value>', got '{line}'")
                    continue
                val = parse_number(args[0], line)
                if not sdll.delete(val):
                    print(f"line {line_num}: {format_val(val)} not found, nothing deleted")

            elif cmd == "exists":
                if len(args) != 1:
                    print(f"line {line_num}: expected 'exists <value>', got '{line}'")
                    continue
                val = parse_number(args[0], line)
                res = sdll.exists(val)
                print(f"exists({format_val(val)}) = {res}")

            elif cmd == "count":
                if len(args) != 1:
                    print(f"line {line_num}: expected 'count <value>', got '{line}'")
                    continue
                val = parse_number(args[0], line)
                c = sdll.count(val)
                print(f"count({format_val(val)}) = {c}")

            elif cmd == "total":
                if len(args) != 0:
                    print(f"line {line_num}: expected 'total', got '{line}'")
                    continue
                print(f"total = {sdll.total()}")

            elif cmd == "median":
                if len(args) != 0:
                    print(f"line {line_num}: expected 'median', got '{line}'")
                    continue
                print(f"median = {sdll.median()}")

            elif cmd == "sum_middle_three":
                if len(args) != 0:
                    print(f"line {line_num}: expected 'sum_middle_three', got '{line}'")
                    continue
                print(f"sum_middle_three = {sdll.sum_middle_three()}")

            elif cmd == "print_list":
                if len(args) != 0:
                    print(f"line {line_num}: expected 'print_list', got '{line}'")
                    continue
                sdll.print_list()

            else:
                print(f"line {line_num}: unknown directive '{cmd}'")

        except ValueError as e:
            print(f"line {line_num}: {e}")

    print("Final list: ", end="")
    sdll.print_list()


if __name__ == "__main__":
    main()