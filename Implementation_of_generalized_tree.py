class GeneralTree:
    def  __init__(self, function=None):
        self.function = function
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def execute(self, number):
        if self.function is not None:
            number = self.function(number)

        for child in self.children:
            number = child.execute(number)

        return number

def add_one(n):
    return n + 1

def multiply_by_two(n):
    return n * 2

tree = GeneralTree(add_one)
child1 = GeneralTree(multiply_by_two)
child2 = GeneralTree(add_one)
child3 = GeneralTree(multiply_by_two)

tree.add_child(child1)
tree.add_child(child2)
child1.add_child(child3)

# Execute the tree
result = tree.execute(3)
print(result)  # Output: 11
