import unittest
from lib.solutions.HLO import hello_solution


class TestSum(unittest.TestCase):
    def test_sum(self):
        assert hello_solution.hello('world') == 'Hello, World!'