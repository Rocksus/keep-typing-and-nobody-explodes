import unittest
from .solver import solve_memory

class TestMemoryModule(unittest.TestCase):
    def test_Memory(self):
        self.assertEqual(solve_memory(1, 3), 'Press the button in the third position')
        self.assertEqual(solve_memory(2, 4), 'Press the button in the same position as stage 1')
        self.assertEqual(solve_memory(3, 4), 'Press the button labeled [4]')
        self.assertEqual(solve_memory(5, 3), 'Press the button with the same label as stage 4')