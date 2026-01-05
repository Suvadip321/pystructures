class Node:
    __slots__ = ("data", "next")

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_start(self, item):
        self.head = Node(item, self.head)
        self.size += 1

    def insert_at_end(self, item):
        n = Node(item)
        if not self.head:
            self.head = n
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = n
        self.size += 1

    def insert_after(self, item, val):
        temp = self.head
        while temp and temp.data != val:
            temp = temp.next

        if not temp:
            raise ValueError("Value not found")

        temp.next = Node(item, temp.next)
        self.size += 1

    def delete_at_start(self):
        if not self.head:
            raise IndexError("Linked list is empty")

        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return item

    def delete_at_end(self):
        if not self.head:
            raise IndexError("Linked list is empty")

        if not self.head.next:
            item = self.head.data
            self.head = None
            self.size -= 1
            return item

        temp = self.head
        while temp.next.next:
            temp = temp.next

        item = temp.next.data
        temp.next = None
        self.size -= 1
        return item

    def delete_node(self, val):
        if not self.head:
            raise IndexError("Linked list is empty")

        if self.head.data == val:
            self.head = self.head.next
            self.size -= 1
            return

        temp = self.head
        while temp.next and temp.next.data != val:
            temp = temp.next

        if not temp.next:
            raise ValueError("Value not found")

        temp.next = temp.next.next
        self.size -= 1

    def __len__(self):
        return self.size

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.data
            temp = temp.next

    def __str__(self):
        return " -> ".join(map(str, self)) or "Empty"

    def __repr__(self):
        return f"SinglyLinkedList([{', '.join(map(str, self))}])"
