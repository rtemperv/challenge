from structures.hash_table import HashTable
import random
import string

def test_create():
    ht = HashTable()
    ht["test"] = 4
    ht["blaat"] = 3

    assert ht._n_items == 2


def test_set():
    ht = HashTable()
    ht["test"] = 4

    assert ht["test"] == 4

    ht["test"] = 342

    assert ht["test"] == 342

    assert ht._n_items == 1


def test_multiple_set():
    ht = HashTable()
    for i in range(200):
        ht[''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))] = random.randint(0,1000)

    assert ht._n_items == 200
    assert ht._n_bits == 9

test_multiple_set()