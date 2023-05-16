class MyList:
    def __init__(self):
        self.data = []

    def append(self, element):
        self.data.append(element)

    def get(self, index):
        if (index >= 0) and index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def set(self, index, value):
        if (index >= 0) and index < len(self.data):
            self.data[index] = value
        else:
            raise IndexError("Index out of range")

    def insert(self, index, value):
        if (index >= 0) and index <= len(self.data):
            self.data.insert(index, value)
        else:
            raise IndexError("Index out of range")

    def search(self, value):
        for i, element in enumerate(self.data):
            if element == value:
                return i
        return -1

    def length(self):
        return len(self.data)
