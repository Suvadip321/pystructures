from typing import Any, Iterator, Optional

class Array:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise Exception("Capacity must be positive")
        self._capacity: int = capacity
        self._data: list[Any] = [None] * capacity
        self._size: int = 0

    def insert(self, item: Any, index: Optional[int] = None) -> None:
        if self._size == self._capacity:
            raise Exception("Array is full")

        if index is None:
            index = self._size
        elif index < 0 or index > self._size:
            raise Exception("Index out of bounds")

        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]

        self._data[index] = item
        self._size += 1

    def delete(self, index: Optional[int] = None) -> Any:
        if self._size == 0:
            raise Exception("Array is empty")

        if index is None:
            index = self._size - 1
        elif index < 0 or index >= self._size:
            raise Exception("Index out of bounds")

        value = self._data[index]

        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._data[self._size - 1] = None
        self._size -= 1
        return value

    def get(self, index: int) -> Any:
        if index < 0 or index >= self._size:
            raise Exception("Index out of bounds")
        return self._data[index]

    def set(self, index: int, value: Any) -> None:
        if index < 0 or index >= self._size:
            raise Exception("Index out of bounds")
        self._data[index] = value

    def __str__(self) -> str:
        return str([self._data[i] for i in range(self._size)])
    
    def __repr__(self) -> str:
        return f"Array(capacity={self._capacity}, elements={self})"

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        for i in range(self._size):
            yield self._data[i]

    def __getitem__(self, index: int) -> Any:
        return self.get(index)

    def __setitem__(self, index: int, value: Any) -> None:
        self.set(index, value)
