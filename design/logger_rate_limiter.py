'''
LeetCode 359. Logger Rate Limiter
https://leetcode.com/problems/logger-rate-limiter/
Design a logger system that receive stream of messages along with its timestamps,
each message should be printed if and only if it is not printed in the last 10 seconds.
Given a message and a timestamp (in seconds granularity),
return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.
Example
Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
'''

from collections import deque

class Logger:
    '''
    Time Complexity: ~N, Space Complexity: ~N
    '''

    def __init__(self):
        ''' Initialize your data structure here.'''
        self.message_set = set()
        self.message_queue = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.message_queue:
            msg, ts = self.message_queue[0]
            if timestamp - ts >= 10:
                self.message_queue.popleft()
                self.message_set.remove(msg)
            else:
                break

        if message not in self.message_set:
            self.message_set.add(message)
            self.message_queue.append((message, timestamp))
            return True
        else:
            return False