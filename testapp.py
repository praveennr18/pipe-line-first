import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1, 1), 2)

if __name__ == "__main__":   # 👈 fixed typo (_name_ → __name__)
    unittest.main()
