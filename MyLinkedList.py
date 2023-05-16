class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert(self, data, position):
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

    def search(self, data):
        current = self.head
        index = 0
        while current is not None:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def delete(self, data):
        if self.is_empty():
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

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

# # Create an instance of LinkedList
# my_list = LinkedList()
#
# # Append elements
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
#
# # Insert an element
# my_list.insert(10, 1)
#
# # Display the list
# my_list.display()  # Output: 1 10 2 3
#
# # Search for an element
# index = my_list.search(2)
# print(index)  # Output: 2
#
# # Delete an element
# my_list.delete(10)
#
# # Display the updated list
# my_list.display()  # Output: 1 2 3
