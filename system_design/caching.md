# Caching
Caching is the process of storing copies of data in a high-speed storage layer (the cache memory) to reduce the time it takes to access this data compared to fetching it directly from the primary storage (the database).

## Benefits of using Caching

1. Reduced Latency
   
   Caching significantly decreases the time it takes to access data, leading to faster response times for user requests.

2. Decreased Network Traffic
   
   By storing frequently accessed data locally, caching reduces the amount of data that must be transmitted over a network, thereby decreasing network congestion.

3. Lower Load on Primary Data Stores
   
   Caching reduces the number of queries to primary data sources like databases, decreasing their load and potentially increasing lifespan.

4. Improved Performance
   
   Applications and systems often experience a general performance boost, as retrieving data from a cache is typically faster than accessing it from primary storage.

5. Increased Throughput
   
   Systems can handle more data and user requests in a given time due to the efficiency gains from caching.

6. Data Availability
   
   In some caching strategies, data can still be available even if the primary data source is temporarily unavailable.

## Types of Caching
1. Client Side / Browser Cache
   
   Caching web content in a browser or device to accelerate content retrieval.

2. CDN Caching (Content Delivery Network)
   
    CDN caching replicates your data across various geographical locations, reducing the data travel time (latency) by serving it from the nearest server to the user.

3. Load Balancer / API Gateway
   
   Balancing incoming network traffic and requests across multiple servers and potentially caching these requests.

4. Database Query Caching
    Database query caching saves the result set of a query in the cache. When the same query is executed, the DBMS first checks the cache. If found, the results are returned from the cache, skipping the actual database hit.

    Database-specific solutions exist, like MySQL Query Cache, or you can use an ORM that includes caching, like Hibernate for Java.

5. In-Memory Caching (e.g., Redis, Memcached)

    Caching data within a single application process.

    In-memory caches store data in RAM, which is much faster than typical disk storage. They are often used for frequently read data, session information, and full-page caching.

6. Distributed Cache
   
   Sharing cache across multiple systems or services.

   Distributed cache is a cache shared across multiple servers, commonly used in Microservices architectures. It improves performance and scalability by replicating cache data across all nodes in a system. Tools like Redis, Memcached, and Hazelcast are popular choices.

## Caching Strategies
1. Cache Aside

    Loading data into the cache on demand. When an application requests data, it first checks the cache. If the data is not found (cache miss), it is fetched from the database and stored in the cache for future requests.

2. Read Through
   
    Data is automatically loaded into the cache from the database when there is a cache miss. The application only interacts with the cache and not directly with the database for read operations.

3. Write Through
   
    Data is written simultaneously to the cache and the database. This ensures data consistency between the cache and database.

4. Write Around

    When data is written, it is written directly to the database and not to the cache. The cache is only updated when data is read.

5. Write Back (Write Behind)
    
    Data is first written to the cache and then, after a certain amount of time or under certain conditions, written back to the database. This allows for batch updates.

### Choosing the Right Caching Strategy
1. Scale of the Application - Larger applications with heavy traffic need more robust caching solutions like CDN or distributed caching.

2. Type of Data - Highly dynamic data might not be the best candidate for caching. On the other hand, data that is expensive to compute or doesn’t change often should be prioritized.
   
3. User Distribution - If users are globally distributed, consider CDN caching. If most of user base is local, in-memory caching may be more effective.
   
4. Infrastructure - Cloud-based applications can take advantage of the built-in caching mechanisms provided by cloud vendors.

## Cache Eviction Policies
Cache eviction policies are critical in caching systems due to the limited size of caches; they ensure optimal use of available space by determining which data to retain or discard.

These policies enhance overall cache performance by keeping the most relevant data accessible while maintaining data accuracy and consistency by removing outdated or less frequently used information.


### Strategies
1. **First In, First Out (FIFO)**: Evicts the oldest items in the cache first, regardless of their usage frequency.
   
2. **Least Recently Used (LRU)**: Evicts the least recently accessed items first, assuming that items not accessed recently are less likely to be accessed in the future.
   
3. **Most Recently Used (MRU)**: Opposite of LRU, it evicts the most recently used items first. This can be useful when the most recent items are less likely to be reaccessed.

4. **Least Frequently Used (LFU)**: Prioritizes eviction of least frequently accessed items, assuming frequent access implies future relevance.
   
5. **Most Frequently Used (MFU)**: Eviction policy is a cache eviction strategy where the cache identifies and removes the data items that are accessed most frequently.
   
6. **Random Replacement (RR)**: Randomly selects a cache item to evict, which can be simpler to implement and effective in specific scenarios.
   
7. **Size-Based Eviction**: Evicts items based on their size to manage the memory footprint, often used in combination with other policies.

## Cache invalidation
Caches often contain data that becomes obsolete or stale. These outdated cache entries need to be identified and slated for removal.

### Strategies
- Time to Live (TTL): Data is invalidated after a specified duration. When the TTL expires, the cached data is either automatically removed or marked as invalid. There are two approaches:
    - Active expiration: A background process or thread periodically scans the cache to check the TTL of cache entries.
    - Passive expiration: Checks the TTL of a cache entry at its access time.
  
- Write-Invalidate: When data is updated in the primary storage, corresponding cache entries are invalidated. This ensures consistency between the cache and the source.
  
- Change Notification: The cache listens for notifications from the data source about changes. When notified, the cache invalidates the relevant entries.

- Polling: The cache periodically checks the validity of its entries by comparing them with the source data.

## Considerations / Challenges

1. **Cache Coherence**  
In distributed systems, multiple caches may store the same data, making it difficult to keep them synchronized.  

   - **Mitigation**  
     Use **write-through** or **write-behind caching** so that updates to the database are automatically reflected in the cache.  
     In multi-node environments, distributed coordination systems such as **Redis Cluster, Consul, or ZooKeeper** help synchronize state across caches.  
     As a fallback, applying a **time-to-live (TTL)** ensures that cached values will eventually expire and refresh, even if updates are missed.  

2. **Cache Invalidation**  
Deciding when and how to update or remove cached data is notoriously hard and often leads to inconsistency.  

   - **Mitigation**  
     The **cache-aside pattern** gives applications direct control of when to populate and invalidate cache entries, improving predictability.  
     **Event-driven invalidation** (e.g., using pub/sub to propagate database changes) ensures caches are updated immediately after writes.  
     When exact consistency is less important, setting **short TTLs** helps maintain freshness while reducing the risk of stale values.  

3. **Stale Data**  
Cached values may become outdated compared to the source of truth, leading to incorrect responses.  

   - **Mitigation**  
     Implement **versioning or etags** so that the cache can confirm whether its data is still valid.  
     Use a **stale-while-revalidate** approach, where slightly outdated data is served while the system refreshes it in the background.  
     For critical operations, bypass the cache entirely and read directly from the source to guarantee accuracy.  

4. **Cache Sizing**  
A cache that’s too small causes frequent evictions, while an oversized cache wastes memory and increases costs.  

   - **Mitigation**  
     Conduct **capacity planning** using traffic data and hit/miss ratio metrics to determine an effective cache size.  
     Leverage **auto-scaling** in cloud environments so cache resources can grow or shrink based on demand.  
     Organize data by priority, ensuring critical or frequently accessed items are always given space.  

5. **Cache Eviction Policies**  
The eviction algorithm (LRU, LFU, FIFO, etc.) determines which data stays in the cache, and a poor choice can degrade performance.  

   - **Mitigation**  
     Match the policy to workload patterns: use **LRU** for workloads where recency matters, or **LFU** where certain items are consistently reused.  
     Test eviction policies against real traffic scenarios to validate that they align with access patterns.  

6. **Data Locality**  
If cached data is stored far from the consumer, latency benefits are reduced or lost.  

   - **Mitigation**  
     Deploy **edge caches or CDNs** to bring data closer to globally distributed users.  
     Use **sharding** strategies to colocate cache nodes with application servers.  
     For low-latency needs across regions, replicate data to caches in multiple locations.  

7. **Scalability**  
As data and traffic grow, caches may become bottlenecks if they cannot scale horizontally.  

   - **Mitigation**  
     Use **distributed caches** such as Redis Cluster or Memcached pools to spread load.  
     Apply **consistent hashing** to evenly distribute keys and minimize data reshuffling.  
     Enable **auto-scaling policies** so new cache nodes can be added dynamically under load.  

8. **Warm-up Time (Cold Cache)**  
After startup, failover, or cache flush, performance drops until frequently accessed data is repopulated.  

   - **Mitigation**  
     Preload the cache with **popular queries or reference data** at startup.  
     Apply **lazy loading with background refresh** to progressively populate data as it is accessed.  
     Use **persistent snapshots** (such as SSD-based cache warming) to restore cache state more quickly after restarts.  

9. **Thundering Herd Problem**  
When a hot item expires, many clients may simultaneously request regeneration, overwhelming backend resources.  

   - **Mitigation**  
     Implement **request coalescing** so that only one client recomputes the value while others wait.  
     Introduce **jittered TTLs** so items don’t expire at the same time.  
     Use **locks or semaphores** to control concurrent recomputations of expensive data.  

10. **Cache Penetration**  
Repeated queries for missing data bypass the cache and directly hit the database, degrading performance.  

    - **Mitigation**  
     Cache **negative results** so that queries for nonexistent data don’t repeatedly reach the database.  
     Use **Bloom filters** or validation checks to block invalid or impossible queries before they reach storage.  
     Apply **rate-limiting** to slow down repeated requests that consistently miss.  

1.  **Hot Key Challenge**  
A few frequently accessed keys create hotspots, leading to load imbalance and degraded performance.  

    - **Mitigation**  
     Replicate hot keys across multiple cache nodes to spread the read load.  
     Introduce **local in-memory caches** within application instances to handle very frequent reads.  
     When possible, **shard data** further (e.g., splitting one key into multiple sub-keys) to distribute access.  

1.  **Cache Poisoning**  
Malicious users may manipulate cached data to serve incorrect or harmful information.  

    - **Mitigation**  
     Apply **input validation and sanitization** before caching responses.  
     Restrict cache writes to trusted sources and enforce **access controls**.  
     Use **digital signatures or checksums** to verify cache content integrity.  

1.  **Monitoring & Observability**  
Without visibility, it’s hard to detect cache inefficiency, failures, or abnormal usage patterns.  

    - **Mitigation**  
     Continuously monitor metrics such as **hit/miss ratios, eviction counts, latency, and error rates**.  
     Configure **alerts** when performance drops below thresholds or anomalies occur.  
     Integrate cache metrics into observability stacks like **Prometheus and Grafana** for real-time dashboards.  

## Examples
1. Redis
2. Memcached
3. Ehcache
4. Apache Ignite

## References
1. https://hackernoon.com/the-system-design-cheat-sheet-cache
2. https://igotanoffer.com/blogs/tech/caching-system-design-interview
3. https://www.educative.io/blog/system-design-caching
   