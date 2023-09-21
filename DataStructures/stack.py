class Stack:
    def __init__(self):
        self.stack = []

    def insert(self, element):
        self.stack.append(element)

    def delete(self):
        self.stack.pop()

    def display(self):
        print(self.stack)


