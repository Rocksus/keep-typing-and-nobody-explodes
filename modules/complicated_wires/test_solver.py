import unittest
from .solver import solve_complicated_wire_letter
from .solver import solve_complicated_wire

class TestComplicatedWires(unittest.TestCase):
    def test_cut(self):
        self.assertEqual(solve_complicated_wire(True,	True,	True,	True,	False,	False,	0), "Do not cut the wire")
        self.assertEqual(solve_complicated_wire(True,	True,	True,	False,	True,	False,	0), "Cut the wire")
        self.assertEqual(solve_complicated_wire(True,	True,	False,	True,	False,	True,	0), "Cut the wire")
        self.assertEqual(solve_complicated_wire(True,	True,	False,	False,	False,	True,	0), "Cut the wire")
        self.assertEqual(solve_complicated_wire(True,	False,	True,	True,	False,	False,	2), "Cut the wire")
        self.assertEqual(solve_complicated_wire(True,	False,	True,	False,	False,	False,	0), "Cut the wire")
        self.assertEqual(solve_complicated_wire(True,	False,	False,	True,	False,	False,	2), "Cut the wire")
        self.assertEqual(solve_complicated_wire(True,	False,	False,	False,	False,	True,	0), "Cut the wire")
        self.assertEqual(solve_complicated_wire(False,	True,	True,	True,	True,	False,	0), "Cut the wire")
        self.assertEqual(solve_complicated_wire(False,	True,	True,	False,	False,	False,	0), "Do not cut the wire")
        self.assertEqual(solve_complicated_wire(False,	True,	False,	True,	True,	False,	0), "Cut the wire")
        self.assertEqual(solve_complicated_wire(False,	True,	False,	False,	False,	True,	0), "Cut the wire")
        self.assertEqual(solve_complicated_wire(False,	False,	True,	True,	False,	False,	2), "Cut the wire")
        self.assertEqual(solve_complicated_wire(False,	False,	True,	False,	False,	False,	0), "Cut the wire")
        self.assertEqual(solve_complicated_wire(False,	False,	False,	True,	False,	False,	0), "Do not cut the wire")
        self.assertEqual(solve_complicated_wire(False,	False,	False,	False,	False,	False,	0), "Cut the wire")
