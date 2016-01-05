from src.structures import Stack
from nose.tools import assert_raises


def test_stack():
    stack = Stack()

    stack.push(5)

    assert len(stack) == 1

    stack.push(2)

    assert len(stack) == 2

    assert stack.peek() == 2

    assert stack.pop() == 2

    assert stack.pop() == 5

    assert_raises(IndexError, stack.pop)

