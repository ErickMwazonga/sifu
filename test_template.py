import unittest


class Solution:

    def get_sum(a, b):
        return a + b


class TestSuite(unittest.TestCase):
    '''AAA - Arrange, Act, Assert'''

    def setUp(self):
        self.soln = Solution

    def test_sum(self):
        # positives
        self.assertEqual(self.soln.get_sum(1, 2), 3)
        self.assertEqual(self.soln.get_sum(11, 12), 23)
        self.assertEqual(self.soln.get_sum(100, 300), 400)

        # negatives
        self.assertEqual(self.soln.get_sum(-1, -9), -10)
        self.assertEqual(self.soln.get_sum(3, -9), -6)

    def test_sum_framework(self):
        # arrange
        soln = Solution

        # act
        summation = soln.get_sum(5, 2)

        # assert
        assert summation == 7
        self.assertEqual(summation, 7)

    def test_sum_all(self):
        soln = Solution

        test_data = [
            {'input': [1, 2], 'output': 3},
            {'input': [11, 12], 'output': 23},
            {'input': [100, 300], 'output': 400},
            {'input': [-1, -9], 'output': -10},
            {'input': [3, -9], 'output': -6}
        ]

        for data in test_data:
            res = soln.get_sum(*data['input'])
            self.assertEqual(res, data['output'])

    @unittest.skip('demonstrating skipping')
    def test_nothing(self):
        # Shouldn't be tested
        ...

    def tearDown(self):
        # close any open generators - files, sockets, connections
        ...


if __name__ == '__main__':
    unittest.main()
