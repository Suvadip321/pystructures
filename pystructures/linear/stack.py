from typing import Any, Iterator

class Stack:
    def __init__(self, max_size: int) -> None:
        if max_size <= 0:
            raise Exception("max_size must be positive")

        self._max_size: int = max_size
        self._data: list[Any] = [None] * max_size
        self._top: int = -1

    def is_empty(self) -> bool:
        return self._top == -1

    def is_full(self) -> bool:
        return self._top == self._max_size - 1

    def push(self, item: Any) -> None:
        if self.is_full():
            raise Exception("Stack overflow")

        self._top += 1
        self._data[self._top] = item

    def pop(self) -> Any:
        if self.is_empty():
            raise Exception("Stack underflow")

        item = self._data[self._top]
        self._top -= 1
        return item

    def peek(self) -> Any:
        if self.is_empty():
            raise Exception("Stack underflow")

        return self._data[self._top]

    def __len__(self) -> int:
        return self._top + 1

    def __iter__(self) -> Iterator[Any]:
        for i in range(self._top + 1):
            yield self._data[i]

    def __str__(self) -> str:
        return str(list(self))

    def __repr__(self) -> str:
        return f"Stack(max_size={self._max_size}, elements={list(self)})"
