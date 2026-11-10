# Assignment 5 - Problem 1
# Name: Anas S.
# Course: CS577 - Data Structures and Algorithms
# Date: 2026-11-09

import random

# Class representing a node in the Binary Search Tree
class Node:
    """ADT representing a Node in a Binary Search Tree."""

    # Constructor for the Node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Class representing the Binary Search Tree
class BinarySearchTree:
    """ADT representing a Binary Search Tree."""

    # Constructor for the Binary Search Tree
    def __init__(self):
        self.root = None

    # Method to add a node to the BST
    def add_node(self, value):
        # Helper function to add a node to the BST
        def _add(curr, val):
            if curr is None:
                return Node(val)
            if val < curr.value:
                curr.left = _add(curr.left, val)
            elif val > curr.value:
                curr.right = _add(curr.right, val)
            return curr

        self.root = _add(self.root, value)

    # Method to delete a node from the BST
    def delete_node(self, value):
        # Helper function to find the minimum value node in a subtree
        def _min_value_node(node):
            current = node
            while current.left is not None:
                current = current.left
            return current

        # Helper function to delete a node from the BST
        def _delete(curr, val):
            if curr is None:
                return None

            if val < curr.value:
                curr.left = _delete(curr.left, val)
            elif val > curr.value:
                curr.right = _delete(curr.right, val)
            else:
                # Case 1 & 2: One child or no child
                if curr.left is None:
                    return curr.right
                elif curr.right is None:
                    return curr.left

                # Case 3: Two children (in-order successor)
                temp = _min_value_node(curr.right)
                curr.value = temp.value
                curr.right = _delete(curr.right, temp.value)

            return curr

        self.root = _delete(self.root, value)

    def find_node(self, value):
        # Search for a node with the specified value
        curr = self.root
        while curr is not None:
            if value == curr.value:
                return True
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return False

    # Method to print the tree structure
    def print_tree(self):
        # Print the tree structure using in-order traversal
        elements = []
        # Helper function to perform in-order traversal
        def _in_order(node):
            if node:
                _in_order(node.left)
                elements.append(str(node.value))
                _in_order(node.right)

        _in_order(self.root)
        print(f"BST (In-Order Traversal): [ {' -> '.join(elements)} ]")


# Demonstration Script
if __name__ == "__main__":
    random.seed(42)  # For reproducible demonstration
    bst = BinarySearchTree()

    # 1. Randomly generate an input set of size between 5 and 50
    input_size = random.randint(5, 50)
    input_set = random.sample(range(1, 1001), input_size)

    print(f"Generated Input Set (Size {input_size}):\n{input_set}\n")

    # 2. Build initial tree
    for val in input_set:
        bst.add_node(val)

    print("- Initial Tree: ")
    bst.print_tree()
    print()

    # 3. Exercise Add Node method
    val_to_add = random.randint(1, 1000)
    print(f"- Adding Node ({val_to_add}): ")
    bst.add_node(val_to_add)
    bst.print_tree()
    print()

    # 4. Exercise Delete Node method
    val_to_delete = input_set[0]
    print(f"- Deleting Existing Node ({val_to_delete}): ")
    bst.delete_node(val_to_delete)
    bst.print_tree()
    print()

    # 5. Exercise Find Node method (Positive Case & Negative Case)
    positive_target = input_set[1]
    negative_target = 9999  # Guaranteed not to exist

    print("- Finding Nodes: ")
    # Positive Case
    found_pos = bst.find_node(positive_target)
    print(
        f"Search for node {positive_target} (Positive Case): {'FOUND' if found_pos else 'NOT FOUND'}"
    )

    # Negative Case
    found_neg = bst.find_node(negative_target)
    print(
        f"Search for node {negative_target} (Negative Case): {'FOUND' if found_neg else 'NOT FOUND'}"
    )