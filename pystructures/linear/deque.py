from typing import Any, Iterator, Optional

class _Node:
    __slots__ = ("data", "prev", "next")

    def __init__(self, data: Any) -> None:
        self.data = data
        self.prev: Optional["_Node"] = None
        self.next: Optional["_Node"] = None

class Deque:
    def __init__(self) -> None:
        self.head: Optional[_Node] = None
        self.tail: Optional[_Node] = None
        self._size: int = 0

    def insert_at_front(self, item: Any) -> None:
        node = _Node(item)

        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self._size += 1

    def insert_at_rear(self, item: Any) -> None:
        node = _Node(item)

        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self._size += 1

    def delete_at_front(self) -> Any:
        if self.head is None:
            raise Exception("Deque is empty")

        value = self.head.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self._size -= 1
        return value

    def delete_at_rear(self) -> Any:
        if self.tail is None:
            raise Exception("Deque is empty")

        value = self.tail.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self._size -= 1
        return value

    def peek_front(self) -> Any:
        if self.head is None:
            raise Exception("Deque is empty")
        return self.head.data

    def peek_rear(self) -> Any:
        if self.tail is None:
            raise Exception("Deque is empty")
        return self.tail.data

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        return f"[{', '.join(map(str, self))}]"

    def __repr__(self) -> str:
        return f"Deque([{', '.join(map(str, self))}])"
