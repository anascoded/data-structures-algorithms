# Assignment 2 - Problem 2 - A
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-10-05

# Node class for singly linked list
class Node:
    """Represents a node in a singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

# Singly linked list implementation
class SinglyLinkedList:
    """Singly linked list with head, tail, and length tracking."""
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # Length of the list
    def __len__(self):
        """Return the number of nodes in the list."""
        return self._size

    # Append a value to the end of the list
    def append(self, value):
        """Add a value to the end of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    # Prepend a value to the front of the list
    def prepend(self, value):
        """Add a value to the front of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1

    # Insert a value at a specific index
    def insert(self, index, value):
        """Add a value at the given index."""
        if not isinstance(index, int) or index < 0 or index > self._size:
            raise IndexError("Index out of range")

        if index == 0: # Prepend if index is 0
            self.prepend(value)
        elif index == self._size:
            self.append(value)
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node = Node(value)
            new_node.next = curr.next
            curr.next = new_node
            self._size += 1

    # Get the value at a specific index
    def get(self, index):
        """Return the value at the given position."""
        if not isinstance(index, int) or index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.value

    # Find the index of the first node with a specific value
    def find(self, value):
        """Return 0-based index of first node with value, or -1 if not found."""
        curr = self.head
        idx = 0
        while curr:
            if curr.value == value:
                return idx
            curr = curr.next
            idx += 1
        return -1

    # Update the value at a specific index
    def update(self, index, value):
        """Replace the value at the given position."""
        if not isinstance(index, int) or index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.value = value

    # Delete the first node with a specific value
    def delete(self, value):
        """Remove the first node holding value. Return True if removed, else False."""
        if self.head is None:
            return False

        if self.head.value == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self._size -= 1
            return True

        curr = self.head
        while curr.next and curr.next.value != value:
            curr = curr.next

        if curr.next is not None:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            self._size -= 1
            return True

        return False

    # Delete the node at a specific index
    def delete_at(self, index):
        """Remove the node at the given index and return its value."""
        if not isinstance(index, int) or index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        if index == 0:
            val = self.head.value
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self._size -= 1
            return val

        curr = self.head
        for _ in range(index - 1):
            curr = curr.next

        val = curr.next.value
        if curr.next == self.tail:
            self.tail = curr
        curr.next = curr.next.next
        self._size -= 1
        return val

    # Print the list from head to tail
    def print_list(self):
        """Print the list from head to tail."""
        if self.head is None:
            print("(empty)")
            return
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.value))
            curr = curr.next
        print(" -> ".join(elements))