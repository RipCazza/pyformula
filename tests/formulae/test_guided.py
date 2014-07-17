import unittest
from pyformula.formulae.guided import abc

class TestGuided(unittest.TestCase):

    def test_abc(self):
        with self.assertRaises(Exception):
            abc(10, 1, 10)
