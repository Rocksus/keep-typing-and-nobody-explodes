import unittest
from .solver import solve_simple_wires

class TestSimpleWireSolver(unittest.TestCase):
    def test_ThreeWires(self):
        input=['yellow', 'yellow', 'black']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the second wire')
        input=['yellow','red','white']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the last wire')
        input=['blue','red','blue']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the last blue wire')
        input=['white','white','red']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the last wire')
    def test_FourWires(self):
        input=['red', 'red', 'yellow', 'yellow']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the last red wire')
        input=['white','black','yellow','yellow']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the first wire')
        input=['white','black','yellow','blue']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the first wire')
        input=['white','yellow','yellow','white']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the last wire')
        input=['white','yellow','black','white']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the second wire')
    def test_FiveWires(self):
        input=['red','blue','yellow','red','black']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the fourth wire')
        input=['red','blue','yellow','blue','yellow']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the first wire')
        input=['red','blue','yellow','red','white']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the second wire')
        input=['black','blue','yellow','red','white']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the first wire')
    def test_SixWires(self):
        input=['red','blue','red','red','black','red']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the third wire')
        input=['red','white','yellow','white','black','red']
        self.assertEqual(solve_simple_wires(input, True), 'Cut the fourth wire')
        input=['blue','blue','blue','white','black','white']
        self.assertEqual(solve_simple_wires(input, False), 'Cut the last wire')
        input=['blue','blue','blue','red','black','white']
        self.assertEqual(solve_simple_wires(input, False), 'Cut the fourth wire')
    def test_Invalid(self):
        input=['red']
        self.assertEqual(solve_simple_wires(input, True), 'Invalid')
