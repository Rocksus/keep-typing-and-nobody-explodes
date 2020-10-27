import unittest
from .solver import solve_morse_code

class TestMorseCode(unittest.TestCase):
    def test_solve_morse(self):
        self.assertEqual(solve_morse_code('.../...././.-../.-../'), '3.505')
        self.assertEqual(solve_morse_code('-/.-./---/-..././...'), '3.545')
        self.assertEqual(solve_morse_code('-..-/./.../-.../---'), '3.535')
        self.assertEqual(solve_morse_code('-.-/.../.-.././.-'), '3.542')
        self.assertEqual(solve_morse_code('-.-/-.../.-././.-/'), '3.572')