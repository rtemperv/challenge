from src.structures import Stack


class SetOfStacks(object):

    def __init__(self, max_size=10):
        self.stacks = [Stack()]
        self.max_size = max_size

    def push(self, value):
        if self.stacks[-1].size() == self.max_size:
            self.stacks.append(Stack())

        self.stacks[-1].push(value)

    def pop(self):

        if self.is_empty():
            raise IndexError()

        if self.stacks[-1].size() == 0:
            self.stacks.pop()

        return self.stacks[-1].pop()

    def is_empty(self):
        return len(self.stacks) == 1 and self.stacks[0].size() == 0
