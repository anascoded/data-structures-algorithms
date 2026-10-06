# Assignment 2 - Problem 4
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-10-05

# Implementation of a sorted doubly linked list with various utility methods.
class Node:
    """Represents a node in a doubly linked list."""
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Implementation of the sorted doubly linked list class.
class SortedDoublyLinkedList:
    """Sorted doubly linked list with head, tail, and size tracking."""
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # Length of the list
    def __len__(self):
        return self._size

    # Insert a value into the list in sorted order
    def add(self, value):
        """Insert value at its correct sorted position."""
        new_node = Node(value)
        self._size += 1

        # If the list is empty, initialize it with the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # Traverse the list to find the correct position for the new node
        curr = self.head
        while curr and curr.value < value:
            curr = curr.next

        # Insert the new node at the correct position
        if curr == self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif curr is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            new_node.next = curr
            new_node.prev = curr.prev
            curr.prev.next = new_node
            curr.prev = new_node

    # Delete a value from the list
    def delete(self, value):
        """Remove one node holding value; return True if removed, False otherwise."""
        curr = self.head
        while curr and curr.value != value:
            if curr.value > value:
                return False
            curr = curr.next

        if curr is None:
            return False

        if curr == self.head and curr == self.tail:
            self.head = None
            self.tail = None
        elif curr == self.head:
            self.head = curr.next
            self.head.prev = None
        elif curr == self.tail:
            self.tail = curr.prev
            self.tail.next = None
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

        self._size -= 1
        return True

    # Check if a value exists in the list
    def exists(self, value):
        """Check if value exists using recursive helper with early stopping."""
        def _exists(node):
            if node is None or node.value > value:
                return False
            if node.value == value:
                return True
            return _exists(node.next)

        return _exists(self.head)

    # Return the total sum of all values in the list
    def total(self):
        """Return sum of all values recursively."""
        def _total(node):
            if node is None:
                return 0
            return node.value + _total(node.next)

        val = _total(self.head)
        return int(val) if isinstance(val, float) and val.is_integer() else val

    # Count occurrences of a value in the list
    def count(self, value):
        """Count occurrences of value recursively with early stopping."""
        def _count(node):
            if node is None or node.value > value:
                return 0
            match = 1 if node.value == value else 0
            return match + _count(node.next)

        return _count(self.head)

    # Return the sum of the three middle nodes in the list
    def sum_middle_three(self):
        """Return sum of the three middle nodes."""
        if self._size < 3:
            raise ValueError("sum_middle_three needs at least 3 nodes")

        mid = self._size // 2
        curr = self.head
        for _ in range(mid):
            curr = curr.next

        if self._size % 2 != 0:
            val = curr.prev.value + curr.value + curr.next.value
        else:
            val = curr.prev.prev.value + curr.prev.value + curr.value

        return int(val) if isinstance(val, float) and val.is_integer() else val

    # Return the median value of the list
    def median(self):
        """Return median value of list."""
        if self._size == 0:
            raise ValueError("median of an empty list")

        mid = self._size // 2
        curr = self.head
        for _ in range(mid):
            curr = curr.next

        if self._size % 2 != 0:
            val = curr.value
            return int(val) if isinstance(val, float) and val.is_integer() else val
        else:
            val = (curr.prev.value + curr.value) / 2.0
            return int(val) if isinstance(val, float) and val.is_integer() else val

    # Print the list from head to tail
    def print_list(self):
        """Print list from head to tail."""
        if self.head is None:
            print("(empty)")
            return

        def _get_elements(node):
            if node is None:
                return []
            val = node.value
            formatted_val = str(int(val)) if isinstance(val, float) and val.is_integer() else str(val)
            return [formatted_val] + _get_elements(node.next)

        # Get the list of formatted values from the recursive helper function
        print(" <-> ".join(_get_elements(self.head)))