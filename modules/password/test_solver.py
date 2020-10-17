import unittest
from .solver import solve_password

class TestPassword(unittest.TestCase):
    def test_solve_password(self):
        self.assertEqual(solve_password([
            ['a','b','c','d','e','f'],
            ['o','e','h','t','a','b'],
            ['e','h','l','i','o','u'],
            ['a','b','c','p','z','o'],
            ['i','h','r','w','e','t']
        ]), ['below'])