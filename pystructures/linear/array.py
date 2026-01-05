class Array:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._capacity = capacity
        self._data = [None] * capacity
        self._size = 0

    def insert(self, item, index=None):
        if self._size == self._capacity:
            raise IndexError("Array is full")

        if index is None:
            index = self._size
        elif index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]

        self._data[index] = item
        self._size += 1

    def delete(self, index=None):
        if self._size == 0:
            raise IndexError("Array is empty")

        if index is None:
            index = self._size - 1
        elif index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        value = self._data[index]

        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._data[self._size - 1] = None
        self._size -= 1
        return value

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._data[index]

    def set(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        self._data[index] = value

    def __str__(self):
        return str([self._data[i] for i in range(self._size)])
    
    def __repr__(self):
        return f"Array(capacity={self._capacity}, elements={self})"

    def __len__(self):
        return self._size

    def __iter__(self):
        for i in range(self._size):
            yield self._data[i]

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        self.set(index, value)
