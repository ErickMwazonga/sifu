'''
Currency Conversion
Resource: https://www.youtube.com/watch?v=L9Me2tDDgY8

Paramenters:
    1. array of currency conversion rates. E.g. ['USD', 'GBP', 0.77] which means 1 USD is equal to 0.77 GBP
    2. an array containing a 'from' currency and a 'to' currency

Given the above parameters, find the conversion rate that maps to the 'from' currency to the 'to' currency.
Your return value should be a number.

Example:
You are given the following parameters:
    1. Rates: ['USD', 'JPY', 110] ['USD', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
    2. To/From currency ['GBP', 'AUD']
    
Find the rate for the 'To/From' curency. In this case, the correct result is 1.89.

# ADJACENCY LIST
{
    'USD': [('JPY', 110), ('AUD', 1.45)], 
    'JPY': [('USD', 0.0091), ('GBP', 0.007)],
    'AUD': [('USD', 0.69)], 
    'GBP': [('JPY', 142.86)]
}


'''
from collections import defaultdict


class CurrencyConverter:

    def create_adjacency_list(self, rates):
        adjacency_list = defaultdict(list)

        for rate in rates:
            to, _from, _rate = rate

            adjacency_list[to].append((_from, _rate))
            adjacency_list[_from].append((to, 1 / _rate))

        return adjacency_list

    def get_conversion(self, rates, queries):
        '''BFS'''

        output = []
        adjacency_list = self.create_adjacency_list(rates)

        for query in queries:
            to, _from = query

            queue = [(to, 1)]
            visited = set([to])
            found = False

            if to not in adjacency_list and _from not in adjacency_list:
                output.append(-1)
                continue

            while queue:
                curr_node, curr_multiplier = queue.pop(0)

                if curr_node == _from:
                    output.append(round(curr_multiplier, 2))
                    found = True
                    break

                for neighbour, multiplier in adjacency_list[curr_node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, multiplier * curr_multiplier))

            if not found:
                output.append(-1)

        return output


rates = [['USD', 'JPY', 110], ['USD', 'AUD', 1.45], ['JPY', 'GBP', 0.0070]]
queries = [['GBP', 'AUD']]

currency_converter = CurrencyConverter()
assert currency_converter.get_conversion(rates, queries) == [1.88]
