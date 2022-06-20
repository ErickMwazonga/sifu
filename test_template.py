import unittest


def get_sum(a, b):
    return a + b


class TestSuite(unittest.TestCase):

    def test_sum(self):
        # positives
        self.assertEqual(get_sum(1, 2), 3)
        self.assertEqual(get_sum(11, 12), 23)
        self.assertEqual(get_sum(100, 300), 400)

        # negatives
        self.assertEqual(get_sum(-1, -9), -10)
        self.assertEqual(get_sum(3, -9), -6)

    def test_sum_all(self):
        test_data = [
            {'input': [1, 2], 'output': 3},
            {'input': [11, 12], 'output': 23},
            {'input': [100, 300], 'output': 400},
            {'input': [-1, -9], 'output': -10},
            {'input': [3, -9], 'output': -6}
        ]

        for data in test_data:
            res = get_sum(*data['input'])
            self.assertEqual(res, data['output'])


if __name__ == '__main__':
    unittest.main()
