# Assignment 2 - Problem 2 - B
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-10-05

import sys
from pathlib import Path

# Ensure the project root is in the system path so that problem2 module can be imported
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from problem2 import SinglyLinkedList


def parse_val(val_str):
    """Attempt integer conversion, fallback to string."""
    try:
        return int(val_str)
    except ValueError:
        return val_str

def main():
    sll = SinglyLinkedList()

    for line_num, line in enumerate(sys.stdin, 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        tokens = line.split()
        cmd = tokens[0]
        args = tokens[1:]

        try:
            if cmd == "append":
                if len(args) != 1:
                    print(f"line {line_num}: append expects 1 argument")
                    continue
                sll.append(parse_val(args[0]))

            elif cmd == "prepend":
                if len(args) != 1:
                    print(f"line {line_num}: prepend expects 1 argument")
                    continue
                sll.prepend(parse_val(args[0]))

            elif cmd == "insert":
                if len(args) != 2 or not args[0].isdigit():
                    print(f"line {line_num}: index must be a whole number, got insert '{args[0]}'")
                    continue
                sll.insert(int(args[0]), parse_val(args[1]))

            elif cmd == "get":
                if len(args) != 1 or not args[0].isdigit():
                    print(f"line {line_num}: invalid get argument")
                    continue
                idx = int(args[0])
                val = sll.get(idx)
                print(f"get ({idx}) = {val}")

            elif cmd == "find":
                if len(args) != 1:
                    print(f"line {line_num}: find expects 1 argument")
                    continue
                pos = sll.find(parse_val(args[0]))
                print(f"find {args[0]} = {pos}")

            elif cmd == "len":
                if len(args) != 0:
                    print(f"line {line_num}: len expects no arguments")
                    continue
                print(f"len = {len(sll)}")

            elif cmd == "update":
                if len(args) != 2 or not args[0].isdigit():
                    print(f"line {line_num}: expected 'update <index> <value>', got update '{line}'")
                    continue
                sll.update(int(args[0]), parse_val(args[1]))

            elif cmd == "delete":
                if len(args) != 1:
                    print(f"line {line_num}): delete expects 1 argument")
                    continue
                success = sll.delete(parse_val(args[0]))
                if not success:
                    print(f"line {line_num}): nothing found, nothing deleted")

            elif cmd == "delete_at":
                if len(args) != 1 or not args[0].isdigit():
                    print(f"line {line_num}: invalid delete_at argument")
                    continue
                val = sll.delete_at(int(args[0]))
                print(f"delete at ({args[0]}) = {val}")

            elif cmd == "print_list":
                if len(args) != 0:
                    print(f"line {line_num}: print_list expects no arguments")
                    continue
                sll.print_list()

            else:
                print(f"line {line_num}: unknown directive '{cmd}'")

        except (IndexError, ValueError) as e:
            print(f"line {line_num}: {e}")

    print("Final list: ", end="")
    sll.print_list()

# Entry point for the script
if __name__ == "__main__":
    main()