#!/usr/bin/python3
"""Define a class Node and SinglyLinkedList."""


class Node:
    """Represent a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new instance of the class.

        Args:
            data: The data of the node.
            next_node: The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """Represent a singly linked list."""

    def __init__(self):
        """Initialize a new instance of the class."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new node into the correct sorted position in the list.

        Args:
            value: The value of the new node.
        """
        new_node = Node(value)

        if not self.head or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Print the entire list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
