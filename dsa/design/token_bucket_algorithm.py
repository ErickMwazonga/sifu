'''
Token Bucket Algorithm
- https://www.youtube.com/watch?v=YXkOdWBwqaA
- https://medium.com/@mojimich2015/token-bucket-algorithm-rate-limiting-explained-with-python-go-73a9f192fda3


The Token Bucket algorithm is a rate-limiting technique used to control how often an action 
can happen (like API requests, network packets, login attempts, etc.).

📌 Core Idea
    - Tokens are added to a 'bucket' at a fixed rate.
    - The bucket has a maximum capacity.
    - Every time an action happens, it consumes 1 token (or more).
    - If there are no tokens available → the action is denied.

🧠 Example
Bucket capacity = 10 tokens
Refill rate = 5 tokens per second

This means:
    - You can instantly make 10 requests (burst).
    - After that, you can make 5 requests per second.

🔴 What Problem Does the Lock Prevent?
If multiple threads call allow_request() at the same time:
    - They may read the same self.tokens value
    - They may both think enough tokens are available
    - They may both subtract tokens
    - Result → more requests allowed than intended
>> That breaks rate limiting.

⚠️ Race Condition Example (Without Lock)
Imagine:
    - tokens = 1
    - Two threads call allow_request() simultaneously

Without a lock:
    - Thread A checks → sees tokens = 1
    - Thread B checks → sees tokens = 1
    >> Both subtract 1
    >> Now tokens = -1
>> You just allowed 2 requests when only 1 should pass.

🧠 Why Exactly We Lock Here
In allow_request() we do multiple related operations
This sequence must be atomic (all-or-nothing).
The lock ensures:
    - Only one thread updates tokens at a time
    - Refill and subtraction happen safely
    - State remains consistent
'''

import time
import threading

class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float):
        '''
        :param capacity: Maximum number of tokens in the bucket
        :param refill_rate: Tokens added per second
        '''
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill_time = time.time()
        self.lock = threading.Lock()

    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill_time

        # Add tokens based on elapsed time
        tokens_to_add = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)

        self.last_refill_time = now

    def allow_request(self, tokens_required: float = 1) -> bool:
        with self.lock:
            self._refill()

            if self.tokens >= tokens_required:
                self.tokens -= tokens_required
                return True
            return False


# Usage
bucket = TokenBucket(capacity=5, refill_rate=2)  # 2 tokens per second

for i in range(10):
    action = 'allowed' if bucket.allow_request() else 'denied'
    print(f"Request {i} {action}")

    time.sleep(0.3)
