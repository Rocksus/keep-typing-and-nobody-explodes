import unittest
from .solver import solve_button_press
from .solver import solve_button_strip

class TestButton(unittest.TestCase):
    def test_release_immediate(self):
        self.assertEqual(solve_button_press('DETONATE', 'black', 'frk', False, 2), 'Press and immediately release the button')
        self.assertEqual(solve_button_press('hold', 'black', 'frk', True, 3), 'Press and immediately release the button')
        self.assertEqual(solve_button_press('hold', 'red', 'frk', False, 3), 'Press and immediately release the button')
    def test_hold(self):
        self.assertEqual(solve_button_press('hold', 'black', 'gth', False, 1), 'Hold and check label strip color')
    def test_release(self):
        self.assertEqual(solve_button_strip('blue'), 'Release when the countdown timer has a 4 in any position')
        self.assertEqual(solve_button_strip('yellow'), 'Release when the countdown timer has a 5 in any position')
        self.assertEqual(solve_button_strip('red'), 'Release when the countdown timer has a 1 in any position')