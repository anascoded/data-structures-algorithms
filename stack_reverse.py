# Assignment 3 - Problem 3
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-10-12

import sys


# Array-Based Stack
class ArrayStack:
    def __init__(self):
        self._data = []

    # Add a value to the top of the stack
    def push(self, val):
        self._data.append(val)

    # Remove and return the value at the top of the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    # Check the value at the top of the stack without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    # Check if the stack is empty
    def is_empty(self):
        return len(self._data) == 0

    # Return a string representation of the stack from top to bottom
    def __str__(self):
        return ", ".join(map(str, self._data))


# Singly Linked List Stack
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Singly linked list stack implementation
class SinglyLinkedListStack:
    def __init__(self):
        self.top = None

    # Add a value to the top of the stack
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    # Remove and return the value at the top of the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        val = self.top.value
        self.top = self.top.next
        return val

    # Check the value at the top of the stack without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Return a string representation of the stack from top to bottom
    def __str__(self):
        elems = []
        curr = self.top
        while curr:
            elems.append(curr.value)
            curr = curr.next
        elems.reverse()
        return ", ".join(map(str, elems))


# Doubly Linked List Stack
class DNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Doubly linked list stack implementation
class DoublyLinkedListStack:
    def __init__(self):
        self.top = None

    # Add a value to the top of the stack
    def push(self, val):
        new_node = DNode(val)
        if self.top is not None:
            self.top.next = new_node
            new_node.prev = self.top
        self.top = new_node

    # Remove and return the value at the top of the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        val = self.top.value
        self.top = self.top.prev
        if self.top is not None:
            self.top.next = None
        return val

    # Check the value at the top of the stack without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Return a string representation of the stack from top to bottom
    def __str__(self):
        elems = []
        curr = self.top
        while curr:
            elems.append(curr.value)
            curr = curr.prev
        elems.reverse()
        return ", ".join(map(str, elems))

# Recursive Stack Reversal
def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(temp)

# Recursively reverses a stack in-place without using loops
def reverse_stack(stack):
    """Reverses a stack in-place using recursion without loops."""
    if not stack.is_empty():
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

# Run the stack reversal for a given stack implementation and input numbers
def run_implementation(stack_cls, name, numbers):
    print(f"- {name}: ")
    s = stack_cls()
    for num in numbers:
        s.push(num)

    print(f"Before:  {s}")
    reverse_stack(s)
    print(f"After:   {s}\n")

# main function to read input and run stack reversal for all three implementations
def main():
    raw_input = sys.stdin.read()
    if not raw_input.strip():
        numbers = list(range(1, 11))
    else:
        tokens = raw_input.replace(',', ' ').split()
        numbers = [int(t) for t in tokens]

    # Run for all three stack implementations
    run_implementation(ArrayStack, "Array Stack", numbers)
    run_implementation(SinglyLinkedListStack, "Singly Linked List Stack", numbers)
    run_implementation(DoublyLinkedListStack, "Doubly Linked List Stack", numbers)

# Entry point for the script
if __name__ == "__main__":
    main()