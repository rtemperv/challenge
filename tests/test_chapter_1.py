from chapter_1 import is_unique, reverse, is_anagram, remove_duplicates, remove_duplicates_better, rotate, expand_zeros, is_rotation
from nose.tools import assert_raises


def test_exercise_1():
    # All unique
    assert is_unique('Tesz')

    # All the same
    assert not is_unique('zzzzzzzzzzzz')

    # Empty string
    assert is_unique('')

    # None
    assert_raises(ValueError, is_unique, None)


def test_exercise_2():
    # Regular string
    assert 'abcdef' == reverse('fedcba')

    # None
    assert_raises(ValueError, reverse, None)

    # Empty string
    assert '' == reverse('')


def test_exercise_3():
    # Empty string
    assert is_anagram('', '')

    # Regular string
    assert is_anagram('kaasblok', 'kolbsaak')

    # None
    assert_raises(TypeError, is_anagram, None, 'test')
    assert_raises(TypeError, is_anagram, 'test', None)
    assert_raises(TypeError, is_anagram, None, None)

def test_exercise_4():
    # empty string
    assert remove_duplicates("") == ""

    # All the same
    assert remove_duplicates("aaaaaaa") == 'a'

    assert remove_duplicates("abcdabcd") == 'abcd'

    assert_raises(TypeError, remove_duplicates, None)

    # empty string
    assert remove_duplicates_better("") == ""

    # All the same
    assert remove_duplicates_better("aaaaaaa") == 'a'

    assert remove_duplicates_better("abcdabcd") == 'abcd'

    assert_raises(TypeError, remove_duplicates_better, None)


def test_exercise_5():

    assert rotate([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]

    assert_raises(TypeError, rotate, None)
    assert_raises(ValueError, rotate, [[2], [1]])
    assert_raises(ValueError, rotate, [[2, 1]])


def test_exercise_6():
    a = [[1, 2, 3], [7, 0, 3], [7, 8, 9]]
    expand_zeros(a)
    assert a == [[1, 0, 3], [0, 0, 0], [7, 0, 9]]

    b = [[1, 2, 3, 4, 0, 6]]
    expand_zeros(b)
    assert b == [[0]*6]


def test_exercise_7():
    assert not is_rotation('acb', 'dfoeabcsde')
    assert is_rotation('banana', 'nanaba')
    assert is_rotation('', '')
    assert_raises(TypeError, is_rotation, None, '')