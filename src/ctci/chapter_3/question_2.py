from src.structures import Stack


class CustomStack(Stack):

    def __init__(self):
        super().__init__()

        self.min_stack = Stack()

    def push(self, value):

        # Keep track of the min value
        if self.min_stack.is_empty() or self.min_stack.peek() >= value:
            self.min_stack.push(value)

        super().push(value)

    def pop(self):

        value = super().pop()

        if value == self.min_stack.peek():
            self.min_stack.pop()

        return value

    def get_minimum(self):
        if not self.min_stack.is_empty():
            return self.min_stack.peek()
