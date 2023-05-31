class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        if capacity < 0 :
            raise ValueError("Invalid Capacity")
        self._size = 0

    def __str__(self):
        return ("🍪" * self.size)

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies.")
        else:
            self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("You asked for more cookies than there are in the Jar")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size