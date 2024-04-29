"""Utility functions for working with Linked Lists."""

from __future__ import annotations

author = "730711485"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Node | None

    def __init__(self, data: int, next: Node | None):
        """Construct a singly linked list. Use None for second argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produde a string visulaization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Return data of first element."""
        return self.data
    
    def tail(self) -> Node:
        """Return a linked list of every element minus the head."""
        return self.next
    
    def last(self) -> int:
        """Return data of last element."""
        if self.next is None:
            return self
        else:
            """calling the same function."""
            return self.next.last()


#  3 -> 4 -> 5 -> None    
c: Node = Node(5, None)
b: Node = Node(4, c)
a: Node = Node(3, b)

#  0-> 1 -> 2 -> None
node_c: Node = Node(2, None)
node_b: Node = Node(1, node_c)
node_a: Node = Node(0, node_b)