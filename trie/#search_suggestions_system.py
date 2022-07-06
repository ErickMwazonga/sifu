'''
1268. Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/

You are given an array of strings products and a string searchWord.
Design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord.
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
Input: products = ['mobile','mouse','moneypot','monitor','mousepad'], searchWord = 'mouse'
Output: [
    ['mobile', 'moneypot', 'monitor'],
    ['mobile', 'moneypot', 'monitor'],
    ['mouse', 'mousepad'],
    ['mouse', 'mousepad'],
    ['mouse', 'mousepad']
]
Explanation: products sorted lexicographically = ['mobile','moneypot','monitor','mouse','mousepad']
After typing m and mo all products match and we show user ['mobile','moneypot','monitor']
After typing mou, mous and mouse the system suggests ['mouse','mousepad']

Example 2:
Input: products = ['bags','baggage','banner','box','cloths'], searchWord = 'bags'
Output: [['baggage','bags','banner'], ['baggage','bags','banner'], ['baggage','bags'],['bags']]
'''


class Solution:
    def suggestedProducts(self, products, searchWord):
        n, res = len(searchWord), []

        for i in range(n):
            curr_products = []

            for prod in products:
                prefix = searchWord[:i+1]

                if prod.startswith(prefix):
                    curr_products.append(prod)

            curr_products = sorted(curr_products)[:3]
            res.append(curr_products)

        return res
