'''
Print all combinations of phrases formed by picking words from each of the given lists

Given N lists of words, print all combinations of phrases that can be
formed by picking one word each from each of the given lists.

input
arr = [
    ['I', 'You', 'They'],
    ['love', 'hate'],
    ['food', 'games']
]

output
[
    'I love food', 'I love games', 'I hate food', 'I hate games',
    'You love food', 'You love games', 'You hate food', 'You hate games',
    'They love food', 'They love games', 'They hate food', 'They hate games'
]
'''


class Solution:
    def phrases(self, arr):
        res = []
        self.dfs(arr, res, comb='', i=0)
        return res

    def dfs(self, lists, res, comb='', i=0):
        if not lists:
            return

        if i == len(lists):
            res.append(comb)
            return

        for word in lists[i]:
            out = comb + ' ' + word
            self.dfs(lists, res, out, i + 1)
