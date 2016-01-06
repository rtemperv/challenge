from typing import List, Generic, TypeVar, Iterable
from annotation.typed import typechecked
T = TypeVar('T')


class LinkedListNode(Generic[T]):
    def __init__(self, value: T, next_node: 'LinkedListNode'=None):
        self.value = value
        self.next_node = next_node

    def get_next_node(self) -> 'LinkedListNode':
        return self.next_node

    def set_next_node(self, node: 'LinkedListNode'):
        self.next_node = node

    def __str__(self):
        return '{}'.format(self.value)


class LinkedList(Generic[T]):

    node_class = LinkedListNode

    def __init__(self):
        self.head = None  # type: LinkedListNode
        self.tail = None
        self._length = 0

    def __iter__(self):
        return iter(self.to_array())

    def insert(self, index, value):
        node = self.node_class(value)

        if index == len(self):
            self.tail = node

        if index == 0:
            node.set_next_node(self.head)
            self.head = node
            self._length += 1
            return self

        prev_node = self.get(index - 1)
        node.set_next_node(prev_node.get_next_node())
        prev_node.set_next_node(node)
        self._length += 1

    def get(self, index):
        if self.head is None or index < 0 or index >= len(self):
            raise IndexError('Index out of bounds')

        if index == 0:
            return self.head

        node = self.head
        while node.get_next_node():
            next_node = node.get_next_node()
            index -= 1
            if index == 0:
                return next_node
            node = next_node

    def remove(self, index):
        if self.head is None or index < 0 or index >= len(self):
            raise IndexError('Index out of bounds')

        if index == 0:
            node = self.head
            self.head = self.head.get_next_node()
            self._length -= 1
            return node

        node = self.head
        while node.get_next_node():
            next_node = node.get_next_node()
            index -= 1
            if index == 0:
                if not next_node.get_next_node():
                    self.tail = node
                node.set_next_node(next_node.get_next_node())
                self._length -= 1
                return next_node
            node = next_node

    def append(self, value: T):
        if len(self) == 0:
            return self.insert(0, value)
        node = self.node_class(value)
        self.tail.set_next_node(node)
        self.tail = node
        self._length += 1
        return self

    def prepend(self, value: T):
        self.insert(0, value)
        return self

    def get_tail_node(self):
        if self.tail is None:
            raise IndexError('No elements available')
        return self.tail

    @typechecked
    def to_array(self) -> List[T]:
        """
        Convert this linked list to an array
        """
        if self.head is None:
            return []
        node = self.head
        values = [node.value]
        while node.get_next_node():
            node = node.get_next_node()
            values.append(node.value)
        return values

    @typechecked
    def __len__(self) -> int:
        return self._length

    def __contains__(self, item):
        return item in self.to_array()

    def remove_duplicates(self):
        """
        Remove all the duplicates in the linked list. O(n) time, O(n) size
        """
        if not self.head:
            return self

        node = self.head
        values = {node.value}
        while node.get_next_node():
            next_node = node.get_next_node()
            if next_node.value in values:
                node.set_next_node(next_node.get_next_node())
                if not next_node.get_next_node():
                    self.tail = node
                self._length -= 1
            else:
                values.add(next_node.value)
                node = node.get_next_node()
        return self

    @typechecked
    def get_nth_to_last(self, n: int) -> Iterable[T]:

        node = self.get(n)
        if not node:
            return
        yield node.value
        while node.get_next_node():
            node = node.get_next_node()
            yield node.value

    @classmethod
    def from_array(cls, array: List[T]) -> 'LinkedList':
        """
        Construct a new linked list from a given array
        :rtype LinkedList
        """
        linked_list = cls()
        for i in array:
            linked_list.append(i)
        return linked_list

    def __add__(self, other):
        """
        Sum two linked list where a linked list represents a number
        """
        a = self.head
        b = other.head

        new_tree = self.__class__()
        carry_over = 0

        while a is not None or b is not None or carry_over:
            summed = (a.value if a else 0) + (b.value if b else 0) + carry_over
            rest = summed % 10
            new_tree.append(rest)
            carry_over = (summed - rest)/10
            a = a.get_next_node() if a else None
            b = b.get_next_node() if b else None
        return new_tree

    def find_loop(self):
        """
        Find the root of a circular list in the linked list
        :return:
        :rtype:
        """
        if self.head is None:
            return None
        a = {self.head}
        next_node = self.head.get_next_node()
        while next_node is not None:
            if next_node in a:
                return next_node
            a.add(next_node)
            next_node = next_node.get_next_node()
        return None

    def merge(self, linked_list: 'LinkedList'):
        if len(self) == 0:
            self.head = linked_list.head
            self.tail = linked_list.tail
            self._length = linked_list._length

        if len(linked_list) == 0:
            return

        self.get_tail_node().set_next_node(linked_list.head)
        self.tail = linked_list.tail
        self._length += len(linked_list)

    def __str__(self) -> str:
        return "[" + (" -> ".join(map(str, self.to_array()))) + "]"
