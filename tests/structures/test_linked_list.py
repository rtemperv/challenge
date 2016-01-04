from code.structures import LinkedList
from nose.tools import assert_raises


def test_linked_list_get():
    ll = LinkedList.from_array([1, 2, 3, 4])

    assert ll.get(3).value == 4

    assert ll.get(0).value == 1

    assert len(ll) == 4

    assert_raises(IndexError, ll.get, 4)


def test_linked_list_remove():
    ll = LinkedList.from_array([2, 3, 4, 5, 6])

    assert len(ll) == 5

    ll.remove(0)

    assert ll.to_array() == [3, 4, 5, 6]
    assert len(ll) == 4

    ll.remove(3)

    assert ll.to_array() == [3, 4, 5]
    assert len(ll) == 3

    assert_raises(IndexError, ll.remove, 3)


def test_linked_list_insert():
    ll = LinkedList.from_array([1, 2, 3])

    ll.insert(0, 4)

    assert ll.to_array() == [4, 1, 2, 3]
    assert len(ll) == 4

    ll.insert(4, 10)

    assert ll.to_array() == [4, 1, 2, 3, 10]
    assert len(ll) == 5


def test_linked_list_iter():
    ll = LinkedList.from_array([1, 2, 3])

    assert list(ll) == [1, 2, 3]