import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def print_items(self):
        for item in self.stack:
            print(item)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def print_items(self):
        for item in self.queue:
            print(item)


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack contains:")
    stack.print_items()

    print("popping an item from the stack returns: ", stack.pop())

    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Queue contains:")
    queue.print_items()

    print("dequeueing an item from the queue returns: ", queue.dequeue())

    sys.exit(0)
