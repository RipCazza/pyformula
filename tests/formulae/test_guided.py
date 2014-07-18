import unittest
from pyformula.formulae import guided



class TestGuided(unittest.TestCase):

    def test_abc(self):
        with self.assertRaises(Exception):
            guided.abc(10, 1, 10)
        self.assertEqual(guided.abc(2, 4, 2)[-1].ans, "-1.0 V -1.0")

    def test_exponential_sum(self):
        self.assertEqual(guided.exponential_sum(8, 2, 1)[0][0], 8**3)

    def test_value_percentage(self):
        self.assertEqual(guided.value_percentage(50, 100)[0][0], 50)

if __name__ == "__main__":
    unittest.main()
