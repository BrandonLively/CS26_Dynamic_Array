class DynamicArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count >= self.capacity:
            print('ERROR: Array is full')
            return

        if index >= self.count:
            print('Error: Index out of range')
            return

        for i in range(self.storage, index-1):
            self.storage[i] = self.storage[i-1]

        self.storage[index] = value
        self.count += 1
