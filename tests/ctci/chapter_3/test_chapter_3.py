import unittest
from src.structures import Stack
from src.ctci.chapter_3.question_2 import CustomStack
from src.ctci.chapter_3.question_3 import SetOfStacks
from src.ctci.chapter_3.question_5 import CustomQueue
from src.ctci.chapter_3.question_6 import sort_stack
import random


class TestChapter3(unittest.TestCase):

    def setUp(self):
        self.stack = CustomStack()

    def test_question_2(self):
        numbers = []
        for i in range(10):
            random_number = random.randint(0, 100)
            self.stack.push(random_number)
            numbers.append(random_number)

        while not self.stack.is_empty():

            assert self.stack.get_minimum() == min(numbers)
            a = self.stack.pop()
            b = numbers.pop()
            assert a == b

    def test_question_3(self):
        stack = SetOfStacks()
        numbers = []
        for i in range(10):
            random_number = random.randint(0, 100)
            stack.push(random_number)
            numbers.append(random_number)

        while not stack.is_empty():
            a = stack.pop()
            b = numbers.pop()
            assert a == b

        with self.assertRaises(IndexError):
            stack.pop()

    def test_question_5(self):

        queue = CustomQueue()

        numbers = []
        for i in range(10):
            random_number = random.randint(0, 100)
            queue.enqueue(random_number)
            numbers.append(random_number)
        numbers.reverse()
        while not queue.is_empty():
            a = queue.dequeue()
            b = numbers.pop()
            assert a == b

    def test_question_6(self):
        stack = Stack()
        numbers = []
        for i in range(10):
            random_number = random.randint(0, 100)
            stack.push(random_number)
            numbers.append(random_number)

        sort_stack(stack)

        for i in sorted(numbers):
            assert i == stack.pop()
