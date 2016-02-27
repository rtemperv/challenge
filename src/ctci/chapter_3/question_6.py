from src.structures import Stack


def sort_stack(stack: Stack):

    extra_stack = Stack()

    while not stack.is_empty():

        element = stack.pop()

        elements_transfered = 0
        while not extra_stack.is_empty() and extra_stack.peek() > element:
            elements_transfered += 1
            stack.push(extra_stack.pop())

        extra_stack.push(element)

        for _ in range(elements_transfered):
            extra_stack.push(stack.pop())

    while not extra_stack.is_empty():
        stack.push(extra_stack.pop())
