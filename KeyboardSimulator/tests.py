import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
        pass


if __name__ == '__main__':
    unittest.main()
