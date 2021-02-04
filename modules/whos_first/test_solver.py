import unittest
from .solver import solve_label_pos
from .solver import solve_possible_answers

class TestWhosFirstSolver(unittest.TestCase):
    def test_LabelPos(self):
        self.assertEqual(solve_label_pos('YES'), 'left-2')
        self.assertEqual(solve_label_pos(''), 'left-3')
        self.assertEqual(solve_label_pos('you are'), 'right-3')
        self.assertEqual(solve_label_pos('you\'re'), 'right-2')
        self.assertEqual(solve_label_pos('no'), 'right-3')
    
    def test_PossibleAnswers(self):
        self.assertIn(solve_possible_answers('blank'), 'okay')
        self.assertIn(solve_possible_answers('you are'), 'what?')
        self.assertIn(solve_possible_answers('uh uh'), 'uh uh')
        self.assertIn(solve_possible_answers('what?'), 'you\'re')
        self.assertIn(solve_possible_answers('you\'re'), 'you')
        self.assertIn(solve_possible_answers('LikE'), 'u')