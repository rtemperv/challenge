import unittest
from src.algorithms import knuth_morris_pratt
import random
import string


class TestStrings(unittest.TestCase):

    def test_knutt_moris_pratt(self):

        for _ in range(20):

            corpus = "".join([random.choice("abcde") for _ in range(40)])
            word = "".join([random.choice("abcde") for _ in range(3)])

            index = knuth_morris_pratt(word, corpus)
            assert index == corpus.find(word)

