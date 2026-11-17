# Assignment 6 - Problem 2
# Name: Anas S.
# Course: CS526 - Data Structures and Algorithms
# Date: 2026-11-16

import ast
import sys

class HeapNode:

    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

# LinkedMinHeap is a linked representation of a binary min-heap.
class LinkedMinHeap:

    def __init__(self):
        self.root = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty heap")
        return self.root.value

    def _get_node_at(self, pos):
        """Navigate to 1-based position `pos` in O(log n) time using binary bits."""
        if pos < 1 or pos > self._size:
            return None
        if pos == 1:
            return self.root

        # Strip '0b1' prefix; remaining bits give path from root (0=left, 1=right)
        path = bin(pos)[3:]
        curr = self.root
        for bit in path:
            curr = curr.left if bit == "0" else curr.right
        return curr

    def _sift_up(self, node):
        # Strictly smaller than parent to preserve insertion stability
        while node.parent is not None and node.value < node.parent.value:
            node.value, node.parent.value = node.parent.value, node.value
            node = node.parent

    def _sift_down(self, node):
        while node.left is not None:
            smallest = node.left
            if node.right is not None and node.right.value < smallest.value:
                smallest = node.right

            if smallest.value < node.value:
                node.value, smallest.value = smallest.value, node.value
                node = smallest
            else:
                break

    def insert(self, value):
        self._size += 1
        new_node = HeapNode(value)

        if self._size == 1:
            self.root = new_node
            return

        parent = self._get_node_at(self._size // 2)
        new_node.parent = parent
        if self._size % 2 == 0:
            parent.left = new_node
        else:
            parent.right = new_node

        self._sift_up(new_node)

    def extract_min(self):
        if self.is_empty():
            raise IndexError("extract_min from an empty heap")

        min_val = self.root.value

        if self._size == 1:
            self.root = None
            self._size = 0
            return min_val

        last_node = self._get_node_at(self._size)
        self.root.value = last_node.value

        # Detach last_node from its parent
        if last_node.parent.left is last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None

        self._size -= 1
        self._sift_down(self.root)
        return min_val

    def _find_node(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        # Pruning: in a min-heap, if node.value > value, subtree cannot contain value
        if node.value > value:
            return None

        left_res = self._find_node(node.left, value)
        if left_res is not None:
            return left_res
        return self._find_node(node.right, value)

    def delete(self, value):
        target = self._find_node(self.root, value)
        if target is None:
            return False

        if self._size == 1:
            self.root = None
            self._size = 0
            return True

        last_node = self._get_node_at(self._size)

        # Detach last_node
        if last_node.parent.left is last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None
        self._size -= 1

        if target is not last_node:
            target.value = last_node.value
            if target.parent is not None and target.value < target.parent.value:
                self._sift_up(target)
            else:
                self._sift_down(target)

        return True

    def build(self, values):
        """Build the heap in O(n) time using bottom-up heapify."""
        self.root = None
        self._size = 0
        if not values:
            return

        # Build complete binary tree structure via linked references
        self.root = HeapNode(values[0])
        self._size = len(values)
        # Temporary queue of parent pointers used strictly to wire links in O(n)
        parents = [self.root]
        head = 0

        for i in range(1, len(values)):
            parent = parents[head]
            node = HeapNode(values[i], parent=parent)
            if parent.left is None:
                parent.left = node
            else:
                parent.right = node
                head += 1
            parents.append(node)

        # Floyd's bottom-up heapification from last internal node down to root
        for pos in range(self._size // 2, 0, -1):
            self._sift_down(self._get_node_at(pos))

    def _clone(self):
        copy_heap = LinkedMinHeap()
        if self.root is None:
            return copy_heap

        def clone_subtree(node, parent=None):
            if node is None:
                return None
            new_n = HeapNode(node.value, parent=parent)
            new_n.left = clone_subtree(node.left, new_n)
            new_n.right = clone_subtree(node.right, new_n)
            return new_n

        copy_heap.root = clone_subtree(self.root)
        copy_heap._size = self._size
        return copy_heap

    def heap_sort(self):
        temp = self._clone()
        sorted_vals = []
        while not temp.is_empty():
            sorted_vals.append(temp.extract_min())
        return sorted_vals

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def print_heap(self):
        if self.is_empty():
            print("(empty)")
            return

        h = self._height(self.root)
        # Compute max string width among values to keep spacing clean
        max_w = 1

        def scan_width(node):
            nonlocal max_w
            if node is None:
                return
            max_w = max(max_w, len(str(node.value)))
            scan_width(node.left)
            scan_width(node.right)

        scan_width(self.root)
        unit = max(max_w + 1, 2)
        width = (2**h) * unit
        rows = 2 * h - 1
        canvas = [[" "] * width for _ in range(rows)]

        def fill(node, depth, left_bound, right_bound):
            if node is None:
                return
            mid = (left_bound + right_bound) // 2
            val_str = str(node.value)
            start = mid - len(val_str) // 2
            for idx, ch in enumerate(val_str):
                if 0 <= start + idx < width:
                    canvas[2 * depth][start + idx] = ch

            if node.left is not None:
                left_mid = (left_bound + mid) // 2
                slash_col = (mid + left_mid) // 2
                canvas[2 * depth + 1][slash_col] = "/"
                fill(node.left, depth + 1, left_bound, mid)

            if node.right is not None:
                right_mid = (mid + right_bound) // 2
                backslash_col = (mid + right_mid) // 2
                canvas[2 * depth + 1][backslash_col] = "\\"
                fill(node.right, depth + 1, mid, right_bound)

        fill(self.root, 0, 0, width)
        for row in canvas:
            print("".join(row).rstrip())

# Main function to process input files and print results.
def main():
    raw = sys.stdin.read().strip()
    if not raw:
        return
    values = ast.literal_eval(raw)
    print(f"Input values: {values}")

    heap = LinkedMinHeap()
    for val in values:
        heap.insert(val)
        print(f"\nAfter insert({val}):")
        heap.print_heap()

# Entry point for the script.
if __name__ == "__main__":
    main()