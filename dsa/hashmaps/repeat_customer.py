'''
Given an access log for a feature, count the number of repeat customers. 
In order to filter out the "novelty effect" a repeat customer is defined as a customer who 
has used the feature on more than one day. Each line of the access log is tab delimited with two fields: 
the timestamp of when the customer visited, and the customer id (a 10 byte string). 
The feature writes an entry to the log file as it gets the hits. Below is an example log file.

log_file = [
    '11-Jun-2018 1:00 AM, 1ABCDEFGHI',
    '11-Jun-2018 3:01 AM, 1ABCDEFGHI',
    '11-Jun-2018 4:12 AM, 2ABCDEFGHI',
    '12-Jun-2018 8:23 AM, 3ABCDEFGHI',
    '12-Jun-2018 4:21 PM, 2ABCDEFGHI',
    '13-Jun-2018 1:14 PM, 3ABCDEFGHI'
]

In this example, the repeat customers are "3ABCDEFGHI" and "2ABCDEFGHI". 
The result that your program generates is the count of repeat customers, in this case 2.
'''

from collections import defaultdict

def get_repeat_customers(log_file: list[str]) -> int:
    customers_visit = defaultdict(set)
    for log in log_file:
        date, *_, customer_id = log.split(' ')
        customers_visit[customer_id].add(date)
    
    # repeat_customers = list(filter(lambda x: len(x) > 1, repeat_customers.values())
    repeat_customers = {k: v for k, v in customers_visit.items() if len(v) > 1}
    return len(repeat_customers)

