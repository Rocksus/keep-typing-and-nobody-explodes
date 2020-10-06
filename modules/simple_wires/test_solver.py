import unittest

class TestSimpleWireSolver(unittest.TestCase):
    def test_ThreeWires(self):
        input=['yellow', 'yellow', 'black']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the second wire')
        input=['yellow','red','white']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the last wire')
        input=['blue','white','blue']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the last blue wire')
        input=['white','white','red']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the last wire')
    def test_FourWires(self):
        input=['red', 'red', 'yellow', 'yellow']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the last red wire')
        input=['white','black','yellow','yellow']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the first wire')
        input=['white','black','yellow','blue']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the first wire')
        input=['white','yellow','yellow','white']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the last wire')
        input=['white','yellow','black','white']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the second wire')
    def test_FiveWires(self):
        input=['red','blue','yellow','red','black']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the fourth wire')
        input=['red','blue','yellow','blue','yellow']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the first wire')
        input=['red','blue','yellow','red','white']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the second wire')
        input=['black','blue','yellow','red','white']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the first wire')
    def test_SixWires(self):
        input=['red','blue','red','red','black','red']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the third wire')
        input=['red','white','yellow','white','black','red']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the fourth wire')
        input=['blue','blue','blue','white','black','white']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the last wire')
        input=['blue','blue','blue','red','black','white']
        self.AssertEqual(solve_simple_wires(input, True), 'Cut the fourth wire')
    def test_Invalid(self):
        input=['red']
        self.AssertEqual(solve_simple_wires(input, True), 'Invalid')
