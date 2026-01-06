from typing import Any, Iterator, Optional

class _Node:
    __slots__ = ("data", "next")

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional["_Node"] = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[_Node] = None
        self._size: int = 0

    def insert_at_start(self, item: Any) -> None:
        node = _Node(item)
        node.next = self.head
        self.head = node
        self._size += 1

    def insert_at_end(self, item: Any) -> None:
        node = _Node(item)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

        self._size += 1

    def insert_after(self, item: Any, val: Any) -> None:
        current = self.head
        while current is not None and current.data != val:
            current = current.next

        if current is None:
            raise Exception("Value not found")

        node = _Node(item)
        node.next = current.next
        current.next = node
        self._size += 1

    def delete_at_start(self) -> Any:
        if self.head is None:
            raise Exception("Linked list is empty")

        value = self.head.data
        self.head = self.head.next
        self._size -= 1
        return value

    def delete_at_end(self) -> Any:
        if self.head is None:
            raise Exception("Linked list is empty")

        if self.head.next is None:
            value = self.head.data
            self.head = None
            self._size -= 1
            return value

        current = self.head
        while current.next.next is not None:
            current = current.next

        value = current.next.data
        current.next = None
        self._size -= 1
        return value

    def delete_node(self, val: Any) -> None:
        if self.head is None:
            raise Exception("Linked list is empty")

        if self.head.data == val:
            self.head = self.head.next
            self._size -= 1
            return

        current = self.head
        while current.next is not None and current.next.data != val:
            current = current.next

        if current.next is None:
            raise Exception("Value not found")

        current.next = current.next.next
        self._size -= 1

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        return " -> ".join(map(str, self)) or "Empty"

    def __repr__(self) -> str:
        return f"SinglyLinkedList([{', '.join(map(str, self))}])"
