# Locking
Locking is the process of ensuring that only one client can access a shared resource at a time.

## Use Cases for Distributed Locks
1. Ensuring Consistency When Accessing Shared Resources

    **Example**: A distributed database or cache where multiple nodes need synchronized updates to avoid data corruption.

1. Coordinating Tasks Across Microservices
   
   Distributed locks are crucial in task scheduling or resource allocation scenarios where microservices need to work together without conflicts.

2. Preventing Duplicate Operations:

    **Example**: In event-driven systems, distributed locks prevent the same message or job from being processed more than once.

## Key considerations
1. Granularity of the lock
   
    Locks should be as fine-grained as possible. This means that we want to lock as little as possible to ensure that we're not blocking other clients from accessing other parts of the system. 
    
    > **Example** - if we're updating a user's profile, we want to lock only that user's profile and not the entire user table.


2. Duration of the lock
    Locks should be held for as short a time as possible. This means that we want to lock only for the duration of the critical section. 
    
   > **Example** - if we're updating a user's profile, we want to lock only for the duration of the update and not for the entire request.

3. Crash Handling (TTL, Ephemeral Sessions)
   
    What if the lock holder dies mid-operation? This is the classic reason for TTL or ephemeral sessions:

    - TTL: If the process doesn’t extend the TTL, the lock is auto-freed. Another node can proceed.

    - Ephemeral: The ephemeral node is removed if the session disappears (like in ZooKeeper).

    > Without these, you risk permanent blocking if someone forgets to release or if the holder abruptly goes offline.

4. Single Point of Failure
   
    If you rely on a single Redis instance or a single ZooKeeper node, your lock manager can fail. Always consider using a clustered or highly available setup, such as Redis with sentinel or cluster mode or a ZooKeeper ensemble of three or five nodes.

5. Whether we can bypass the lock
    In many cases, we can avoid locking by employing an "optimistic" concurrency control strategy, especially if the work to be done is either read-only or can be retried. In an optimistic strategy we're going to assume that we can do the work without locking and then check to see if we were right. In most systems, we can use a "compare and swap" operation to do this.

    **Optimistic concurrency control** makes the assumption that most of the time we won't have contention (or multiple people trying to lock at the same time) in a system, which is a good assumption for many systems! That said, not all systems can use optimistic concurrency control. For example, if you're updating a user's bank account balance, you can't just assume that you can do the update without locking.

## How it works
1. Step 1: Lock Request
    
    A node determines it needs exclusive access to a shared resource and communicates with a lock manager (e.g., Redis, ZooKeeper, or a database) that supports TTL or ephemeral locks.

2. Step 2: Acquire Attempt

    - If no lock currently exists, the node creates one, for instance by setting a Redis key with a time-to-live or by creating an ephemeral zNode in ZooKeeper.

    - If another node is holding the lock, this node either waits, fails immediately, or retries, depending on your chosen policy.

3. Step 3: Critical Operation

    After acquiring the lock, the node proceeds with the operation that must not be run in parallel—such as updating a database row, writing to a shared file, or sending a limited external API request.

4. Step 4: Standard Release
   
    Once finished, the node explicitly removes the lock record (e.g., deleting the Redis key or calling an unlock function). At this point, other contenders are free to acquire the lock.

5. Step 5: Crash or Automatic Release
    
    If the node fails or loses its session, the TTL expires, or the ephemeral mechanism detects the node’s absence. The lock manager then removes the lock, automatically merging into the same path as a standard release so a new node can acquire it. This avoids leaving the system stuck with a “zombie” lock that never gets freed.

## Tools for Distributed Locking
1. Redis (and clones)
   
   You store a “lock key” in Redis with a time limit attached. If the lock key doesn’t exist, you create it and claim the lock. Once your task finishes, you remove the key. If your process crashes, Redis removes the key after the time limit expires, so no one stays locked out forever. This method is quick and works well if you already rely on Redis, but you should be cautious about network splits or cluster issues.

   > Redis runs all commands in a single thread, so there is no risk of two commands interfering partway through. If two clients try to create the same lock key simultaneously, Redis processes them in strict sequence: either the first wins or the second does, but never both

2. ZooKeeper / etcd
   
   These tools consistently keep data across a group of servers. You write a small record saying, “I own this lock,” and if you go offline, the system notices and removes your record automatically. ZooKeeper and etcd are often used for more advanced cluster coordination or leader election, so they’re more complex to set up than Redis. However, they offer strong consistency guarantees.

3. Database Locks
   
   If you have a single database (like Postgres or MySQL) where all your data lives, you can let the database control concurrency. You request a named lock, and the database blocks any other request for that same lock name until you release it. It’s convenient if you already use a single DB for everything, but it may not scale well across multiple databases or regions, and frequent locking could cause contention.

## The Complications with Distributed Locking
While distributed locking solves critical issues in distributed systems, it also introduces its own set of challenges:

1. Deadlocks: If two or more operations hold locks and each is waiting for the other to release its lock, we have a deadlock situation.

2. Lock Timeout: What should be the maximum time a process should wait to acquire a lock? A long timeout could lead to process starvation, while a short timeout might cause frequent retry overheads.

3. Failure to Release Locks: If a node fails after acquiring a lock but before releasing it, other nodes waiting for the lock will be stuck indefinitely.

4. Split-Brain Scenario: In the event of a network partition, two nodes might assume that they have the lock, leading to a split-brain scenario and potentially causing data corruption.

## References
1. https://www.architecture-weekly.com/p/distributed-locking-a-practical-guide
2. https://www.alibabacloud.com/blog/implementation-principles-and-best-practices-of-distributed-lock_600811