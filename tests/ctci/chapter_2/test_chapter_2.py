from src.structures import LinkedList
from nose.tools import assert_raises


def test_exercise_1():
    assert LinkedList.from_array([]).remove_duplicates().to_array() == []

    assert LinkedList.from_array([1, 1, 1, 1, 1, 1]).remove_duplicates().to_array() == [1]

    assert LinkedList.from_array([1, 3, 4, 6, 2, 3, 1]).remove_duplicates().to_array() == [1, 3, 4, 6, 2]


def test_exercise_2():
    assert list(LinkedList.from_array([1, 2, 3, 4, 5, 6, 7]).get_nth_to_last(0)) == [1, 2, 3, 4, 5, 6, 7]

    assert list(LinkedList.from_array([1, 2, 3, 4, 5, 6, 7]).get_nth_to_last(5)) == [6, 7]

    assert_raises(IndexError, lambda x: list(LinkedList.from_array([1, 2, 3, 4, 5, 6, 7]).get_nth_to_last(x)), 7)


def test_exercise_3():
    pass

def test_exercise_4():
    linked_list_a = LinkedList.from_array([1, 2, 3])
    linked_list_b = LinkedList.from_array([3, 2, 1])
    linked_list_c = LinkedList.from_array([0, 0, 7, 1])

    assert (linked_list_a + linked_list_b).to_array() == [4, 4, 4]

    assert (linked_list_a + linked_list_c).to_array() == [1, 2, 0, 2]


def test_exercise_5():
    linked_list = LinkedList.from_array([1, 2, 3, 4, 5])

    assert linked_list.find_loop() is None

    # Insert a circular dependency 5 -> 2
    linked_list.get_tail_node().set_next_node(linked_list.head.get_next_node())

    assert linked_list.find_loop().value == 2

    empty_linked_list = LinkedList.from_array([])

    assert_raises(IndexError, empty_linked_list.get_tail_node)


def test_prepend():

    linked_list = LinkedList()
    linked_list.prepend(1)
    linked_list.prepend(2)

    assert linked_list.to_array() == [2, 1]

test_exercise_5()