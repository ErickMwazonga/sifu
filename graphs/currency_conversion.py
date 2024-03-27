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

from collections import defaultdict, deque

class CurrencyConverter_DFS:

    def build_graph(self, rates):
        graph = defaultdict(list)
        for rate in rates:
            from_currency, to_currency, value = rate
            graph[from_currency].append((to_currency, value))
            graph[to_currency].append((from_currency, 1 / value))
        return graph

    def calculate_conversion_rates(self, rates, from_currency, to_currency):
        # Build graph
        graph = self.build_graph(rates)
            
        # Perform DFS for each query
        visited = set()
        rate = self.dfs(graph, from_currency, to_currency, 1.0, visited)
        return rate
        
    def dfs(self, graph, start, end, rate, visited):
        # if no path to destination is found
        if start not in graph or start in visited:
            return -1.0
        if start == end:
            return rate
        
        visited.add(start)
        neighbors = graph[start]
        for neighbor, neighbor_value in neighbors:
            rate = self.dfs(graph, neighbor, end, rate * neighbor_value, visited)
            if rate != -1.0:
                return rate
        return -1.0



class CurrencyConverter_BFS:

    def create_adjacency_list(self, rates):
        adjacency_list = defaultdict(list)

        for rate in rates:
            to, _from, _rate = rate

            adjacency_list[to].append((_from, _rate))
            adjacency_list[_from].append((to, 1 / _rate))

        return adjacency_list
    
    def get_conversion(self, rates, to, _from):
        graph = self.create_adjacency_list(rates)

        queue = deque([(_from, 1)])
        visited = set([_from])

        if to not in graph or _from not in graph:
            return -1

        while queue:
            curr_node, curr_multiplier = queue.popleft()

            if curr_node == _from:
                return curr_multiplier

            for neighbor, multiplier in graph[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, multiplier * curr_multiplier))

        return -1


rates = [['USD', 'JPY', 110], ['USD', 'AUD', 1.45], ['JPY', 'GBP', 0.0070]]

currency_converter = CurrencyConverter_DFS()
assert currency_converter.get_conversion(rates, 'GBP', 'AUD') == [1.88]
