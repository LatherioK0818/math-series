import unittest
from series import fibonacci, lucas

class TestSequences(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(10), 55)

    def test_lucas(self):
        self.assertEqual(lucas(0), 2)
        self.assertEqual(lucas(1), 1)
        self.assertEqual(lucas(10), 123)

if __name__ == "__main__":
    unittest.main()
