"""
Linear data structures.

Public API:
- Array
- SinglyLinkedList
- DoublyLinkedList
"""

from .array import Array
from .singly_linked_list import SinglyLinkedList
from .doubly_linked_list import DoublyLinkedList
from .stack import Stack
from .queue import Queue

__all__ = [
    "Array",
    "SinglyLinkedList",
    "DoublyLinkedList",
    "Stack",
    "Queue"
]
