class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def insert(self, key, value):
        hash_value = self.hash(key)
        for pair in self.table[hash_value]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hash_value].append([key, value])

    def get(self, key):
        hash_value = self.hash(key)
        for pair in self.table[hash_value]:
            if pair[0] == key:
                return pair[1]
        raise KeyError('Key not found')

    def remove(self, key):
        hash_value = self.hash(key)
        for i, pair in enumerate(self.table[hash_value]):
            if pair[0] == key:
                del self.table[hash_value][i]
                return
        raise KeyError('Key not found')