import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class Stack:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        linked_list = []
        while node is not None:
            linked_list.append(node.data)
            node = node.next
        linked_list.append("None")
        return " -> ".join(linked_list)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def push(self, item):
        if not self.head:
            self.head = Node(item)
        else:
            for current_node in self:
                pass
            current_node.next = Node(item)

    def pop(self):
        for node in self:
            if node.next is None:
                print("Popping an item from the stack returns: ", node.data)
                previous_node.next = None
                return
            previous_node = node

    def print_items(self):
        print("Stack: ", self)


class Queue:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        linked_list = []
        while node is not None:
            linked_list.append(node.data)
            node = node.next
        linked_list.append("None")
        return " -> ".join(linked_list)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def enqueue(self, item):
        if not self.head:
            self.head = Node(item)
            return
        for current_node in self:
            pass
        current_node.next = Node(item)

    def dequeue(self):
        print("Dequeueing an item from the queue returns: ", self.head)
        self.head = self.head.next

    def print_items(self):
        print("Queue: ", self)


if __name__ == "__main__":
    print("\nSTACK\n")
    stack = Stack()
    stack.push("1")
    stack.push("2")
    stack.push("3")
    stack.print_items()
    stack.pop()
    stack.print_items()
    stack.push("4")
    stack.print_items()
    stack.pop()
    stack.print_items()
    print("\nQUEUE\n")
    queue = Queue()
    queue.enqueue("1")
    queue.enqueue("2")
    queue.enqueue("3")
    queue.print_items()
    queue.dequeue()
    queue.print_items()
    queue.enqueue("4")
    queue.print_items()
    queue.dequeue()
    queue.print_items()

    sys.exit(0)
