import unittest
from lib.solutions.CHK import checkout_solution


class TestChk(unittest.TestCase):
    def test_chk_1_A(self):
        assert checkout_solution.hello('A') == 50

    def test_chk_1_A_and_1_B(self):
        assert checkout_solution.hello('AB') == 80

    def test_chk_illegal_item(self):
        assert checkout_solution.hello('G') == -1
