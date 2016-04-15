
class DoublyLinkedListNode(object):

    def __init__(self, number):
        self.next = None
        self.previous = None
        self.data = None
        self.number = number


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None # type: DoublyLinkedListNode
        self.tail = None # type: DoublyLinkedListNode

    def append(self, node: DoublyLinkedListNode) -> None:

        # Empty list
        if not self.tail:
            self.head = self.tail = node
            return

        # All other cases
        self.tail.next = node
        node.previous = self.tail
        self.tail = node

    def flatten(self) -> None:
        node = self.head

        while node:
            next_node = node.next
            if node.data and node.data.head:
                node.data.flatten()

                if next_node:
                    next_node.previous = node.data.tail
                else:
                    self.tail = node.data.tail
                node.next = node.data.head
                node.data.tail.next = next_node
                node.data.head.previous = node

            node = next_node


ll = DoublyLinkedList()
a = DoublyLinkedListNode(1)
b = DoublyLinkedList()

c = DoublyLinkedListNode(2)
d = DoublyLinkedListNode(3)

b.append(c)
b.append(d)

z = DoublyLinkedList()
z.append(DoublyLinkedListNode(8))
d.data = z

a.data = b

ll.append(a)
ll.append(DoublyLinkedListNode(4))

ll.flatten()

node = ll.head
while node:
    print(node.number)
    node = node.next
