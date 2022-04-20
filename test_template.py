import unittest


def get_sum(a, b):
    return a + b


class TestSuite(unittest.TestCase):

    def test_next_bigger(self):
        self.assertEqual(get_sum(1, 2), 3)
        self.assertEqual(get_sum(11, 12), 23)
        self.assertEqual(get_sum(100, 300), 400)

        self.assertEqual(get_sum(-1, -9), -10)
        self.assertEqual(get_sum(3, -9), -6)


if __name__ == '__main__':
    unittest.main()
