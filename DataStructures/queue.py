# FIFO
class Queue:
    def __init__(self, length):
        self.queue = []
        self.length = length

    def enqueue(self, element):
        if len(self.queue) < self.length:
            self.queue.insert(0, element)
        else:
            print("Queue is full!")

    def dequeue(self):
        if len(self.queue) != 0:
            self.queue.pop()
        else:
            print("Queue is Empty!")

    def isFull(self):
        if len(self.queue) < self.length:
            print("Queue is not Full!")
        else:
            print("Queue is Full!")

    def peek(self):
        if len(self.queue) != 0:
            return self.queue.pop()

    def display(self):
        print(self.queue)


class PriorityQueue:
    def __init__(self, length):
        self.queue = []
        self.length = length

    def isFull(self):
        if len(self.queue) == self.length:
            return 1
        else:
            return 0

    def enqueue(self, element):
        pass

    def dequeue(self):
        pass


class CircularQueue:
    def __init__(self, length):
        self.queue = []
        self.length = length

    def isFull(self):
        if len(self.queue) == self.length:
            return 1
        else:
            return 0


class DEQueue:
    def __init__(self, length):
        self.queue = []
        self.length = length

    def isFull(self):
        if len(self.queue) == self.length:
            return 1
        else:
            return 0
