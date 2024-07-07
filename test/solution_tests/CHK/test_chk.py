import unittest
from lib.solutions.CHK import checkout_solution


class TestChk(unittest.TestCase):
    def test_chk_1(self):
        assert checkout_solution.hello('A') == 50

    def test_chk_2(self):
        assert checkout_solution.hello('AB') == 80