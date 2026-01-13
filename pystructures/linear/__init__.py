"""
Linear data structures.

Public API:
- Array
- SinglyLinkedList
- DoublyLinkedList
- Stack
- Queue
- Deque
"""

from .array import Array
from .singly_linked_list import SinglyLinkedList
from .doubly_linked_list import DoublyLinkedList
from .stack import Stack
from .queue import Queue
from .deque import Deque

__all__ = [
    "Array",
    "SinglyLinkedList",
    "DoublyLinkedList",
    "Stack",
    "Queue",
    "Deque"
]
