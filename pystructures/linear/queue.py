from typing import Any, Iterator

class Queue:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise Exception("Capacity must be positive")

        self._capacity: int = capacity
        self._data: list[Any] = [None] * capacity
        self._front: int = 0
        self._rear: int = -1
        self._size: int = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def enqueue(self, item: Any) -> None:
        if self.is_full():
            raise Exception("Queue overflow")

        self._rear = (self._rear + 1) % self._capacity
        self._data[self._rear] = item
        self._size += 1

    def dequeue(self) -> Any:
        if self.is_empty():
            raise Exception("Queue underflow")

        item = self._data[self._front]
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item

    def peek(self) -> Any:
        if self.is_empty():
            raise Exception("Queue underflow")

        return self._data[self._front]

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        idx = self._front
        for _ in range(self._size):
            yield self._data[idx]
            idx = (idx + 1) % self._capacity

    def __str__(self) -> str:
        return str(list(self))

    def __repr__(self) -> str:
        return f"Queue(capacity={self._capacity}, elements={list(self)})"
