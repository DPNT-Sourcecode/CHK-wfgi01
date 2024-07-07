import unittest
from lib.solutions.CHK import checkout_solution


class TestChk(unittest.TestCase):
    def test_chk_1_A(self):
        assert checkout_solution.checkout('A') == 50

    def test_chk_1_A_1_B(self):
        assert checkout_solution.checkout('AB') == 80

    def test_chk_3_A(self):
        assert checkout_solution.checkout('AAA') == 130

    def test_chk_5_A(self):
        assert checkout_solution.checkout('AAAAA') == 200

    def test_chk_6_A(self):
        assert checkout_solution.checkout('AAAAAA') == 250

    def test_chk_8_A(self):
        assert checkout_solution.checkout('AAAAAAAA') == 330

    def test_chk_9_A(self):
        assert checkout_solution.checkout('AAAAAAAAA') == 380

    def test_chk_illegal_item(self):
        assert checkout_solution.checkout('#') == -1

    def test_chk_1_A_1_B_1_E(self):
        assert checkout_solution.checkout('ABE') == 120

    def test_chk_1_A_1_B_2_E(self):
        assert checkout_solution.checkout('ABEE') == 130

    def test_chk_1_A_1_B_3_E(self):
        assert checkout_solution.checkout('ABEEE') == 170

    def test_chk_2_E(self):
        assert checkout_solution.checkout('EE') == 80

    def test_chk_2_F(self):
        assert checkout_solution.checkout('FF') == 20

    def test_chk_3_F(self):
        assert checkout_solution.checkout('FFF') == 20

    def test_chk_4_F(self):
        assert checkout_solution.checkout('FFFF') == 30

    def test_chk_6_F(self):
        assert checkout_solution.checkout('FFFFFF') == 40

