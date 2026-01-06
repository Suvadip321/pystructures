from typing import Any, Iterator, Optional

class _Node:
    __slots__ = ("data", "prev", "next")

    def __init__(self, data: Any) -> None:
        self.data = data
        self.prev: Optional["_Node"] = None
        self.next: Optional["_Node"] = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[_Node] = None
        self._size: int = 0

    def insert_at_start(self, item: Any) -> None:
        node = _Node(item)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
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
            node.prev = current
            current.next = node

        self._size += 1

    def insert_after(self, item: Any, val: Any) -> None:
        current = self.head
        while current is not None and current.data != val:
            current = current.next

        if current is None:
            raise Exception("Value not found")

        node = _Node(item)
        node.prev = current
        node.next = current.next
        current.next = node
        if node.next is not None:
            node.next.prev = node

        self._size += 1

    def delete_at_start(self) -> Any:
        if self.head is None:
            raise Exception("Linked list is empty")

        value = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
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
            if self.head is not None:
                self.head.prev = None
            self._size -= 1
            return

        current = self.head
        while current.next is not None and current.next.data != val:
            current = current.next

        if current.next is None:
            raise Exception("Value not found")

        current.next = current.next.next
        if current.next is not None:
            current.next.prev = current
        self._size -= 1

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        return " <-> ".join(map(str, self)) or "Empty"

    def __repr__(self) -> str:
        return f"DoublyLinkedList([{', '.join(map(str, self))}])"
