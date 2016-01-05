import unittest
from src.extra.infix_to_postfix import infix_to_postfix


class TestInfixToPostfix(unittest.TestCase):

    def test_infix_to_postfix(self):
        assert infix_to_postfix('(A + 5) - 3 / 4') == "A 5 + 3 4 / -"
