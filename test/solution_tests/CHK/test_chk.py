import unittest
from lib.solutions.CHK import checkout_solution


class TestChk(unittest.TestCase):
    def test_chk_1_A(self):
        assert checkout_solution.checkout('A') == 50

    def test_chk_1_A_1_B(self):
        assert checkout_solution.checkout('AB') == 80

    def test_chk_illegal_item(self):
        assert checkout_solution.checkout('G') == -1

    def test_chk_1_A_1_B_1_E(self):
        assert checkout_solution.checkout('ABE') == 120

    def test_chk_1_A_1_B_2_E(self):
        assert checkout_solution.checkout('ABEE') == 190

