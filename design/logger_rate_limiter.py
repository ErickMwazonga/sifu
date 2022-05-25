'''
LeetCode 359. Logger Rate Limiter
Link: https://leetcode.com/problems/logger-rate-limiter/

Design a logger system that receive stream of messages along with its timestamps,
each message should be printed if and only if it is not printed in the last 10 seconds.
Given a message and a timestamp (in seconds granularity),
return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.
Examples
Logger logger = new Logger();

1. logger.shouldPrintMessage(1, 'foo') -> True 
2. logger.shouldPrintMessage(2, 'bar') -> True
3. logger.shouldPrintMessage(3, 'foo') -> False
4. logger.shouldPrintMessage(8, 'bar') -> False
5. logger.shouldPrintMessage(10, 'foo') -> False
6. logger.shouldPrintMessage(11, 'foo') -> True
'''

from collections import deque


class Logger:
    '''Time Complexity: ~N, Space Complexity: ~N'''

    def __init__(self):
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

        if message in self.message_set:
            return False
        else:
            self.message_set.add(message)
            self.message_queue.append((message, timestamp))
            return True
