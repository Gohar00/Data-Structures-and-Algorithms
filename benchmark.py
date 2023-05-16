from datetime import datetime


# Custom List Implementation
class MyList:
    def __init__(self):
        self.data = []

    def append(self, element):
        self.data.append(element)

    def insert(self, index, element):
        self.data.insert(index, element)

    def delete(self, element):
        self.data.remove(element)

    def search(self, element):
        if element in self.data:
            return self.data.index(element)
        return -1


# Linked List Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current is not None and count < position - 1:
                current = current.next
                count += 1
            if current is None:
                raise IndexError("Index out of range")
            new_node.next = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            raise Exception("Cannot delete from an empty list")
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError("Data not found in the list")

    def search(self, data):
        current = self.head
        index = 0
        while current is not None:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

def benchmark(n):
    # Measure time duration for operations in custom list
    custom_list = MyList()

    # Measure insertion time
    start_time = datetime.now()
    for i in range(n):
        custom_list.append(i)
    insertion_time = datetime.now() - start_time

    # Measure deletion time
    start_time = datetime.now()
    for i in range(n):
        custom_list.delete(i)
    deletion_time = datetime.now() - start_time

    # Measure search time
    start_time = datetime.now()
    for i in range(n):
        custom_list.search(i)
    search_time = datetime.now() - start_time

    print(f"Customs list's operation's times for {n} element ")
    print("Insertion Time:", insertion_time.total_seconds(), "seconds")
    print("Deletion Time:", deletion_time.total_seconds(), "seconds")
    print("Search Time:", search_time.total_seconds(), "seconds")
    print()

    # Measure time duration for operations in linked list
    linked_list = LinkedList()

    # Measure insertion time
    start_time = datetime.now()
    for i in range(n):
        linked_list.append(i)
    insertion_time = datetime.now() - start_time

    start_time = datetime.now()
    for i in range(n):
        linked_list.delete(i)
    deletion_time = datetime.now() - start_time

    start_time = datetime.now()
    for i in range(n):
        linked_list.search(i)
    search_time = datetime.now() - start_time

    print(f"Linked List's operation's times for {n} element ")
    print("Insertion Time:", insertion_time.total_seconds(), "seconds")
    print("Deletion Time:", deletion_time.total_seconds(), "seconds")
    print("Search Time:", search_time.total_seconds(), "seconds")
    print()


n = 1000
n1 = 10000
n2 = 100000
benchmark(n)
benchmark(n1)
benchmark(n2)