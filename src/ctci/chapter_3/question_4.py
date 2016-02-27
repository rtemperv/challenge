from src.structures import Stack

def hanoi(n):

    start_stack = Stack()
    start_stack.stack_nr = 1
    for i in reversed(range(n)):
        start_stack.push(i)

    buffer = Stack()
    buffer.stack_nr = 2

    destination = Stack()
    destination.stack_nr = 3

    move_disks(n, destination, buffer, start_stack)


def move_disks(n: int, destination: Stack, buffer: Stack, origin: Stack):

    if n > 0:
        move_disks(n-1, buffer, destination, origin)
        print('{} -> {}'.format(origin.stack_nr, destination.stack_nr))
        destination.push(origin.pop())
        move_disks(n-1, destination, origin, buffer)


