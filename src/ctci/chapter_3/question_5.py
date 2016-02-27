from src.structures import Stack


class CustomQueue():

    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, value):
        while not self.dequeue_stack.is_empty():
            self.enqueue_stack.push(self.dequeue_stack.pop())

        return self.enqueue_stack.push(value)

    def dequeue(self):
        while not self.enqueue_stack.is_empty():
            self.dequeue_stack.push(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def is_empty(self):
        return not self.enqueue_stack.size() and not self.dequeue_stack.size()

