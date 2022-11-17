import arithmetic
import unittest

class AdderTestCase(unittest.TestCase):
    """Examples of unit tests: discrete code testing."""

    def test_adder(self):
        assert arithmetic.adder(2, 3) == 5

    def test_adder_2(self):
        self.assertEqual(arithmetic.adder(2, 2), 4)


if __name__ == "__main__":
    # If called like a script, run our tests
    unittest.main()
