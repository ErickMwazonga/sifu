# Load Balancer

A Load Balancer is like a traffic cop for your servers, evenly distributing incoming network requests across multiple backend instances to prevent any single server from becoming overwhelmed.

## Features/ Benefits of load balancing
1. Availability

    Load balancers perform health checks on servers before routing requests to them. If one server is about to fail, or is offline for maintenance or upgrades, load balancing automatically reroutes the workload to a working server to avoid service interruptions and maintain high availability.

2. Scalability/Traffic Distribution

    Load balancing enables an on-demand, high-performance infrastructure that can handle the heaviest or lightest network traffic loads. Physical or virtual servers can be added or removed as needed, making scalability simple and automated.

3. Security

    Load balancers can include security features such as SSL encryption, web application firewalls (WAF) and multi-factor authentication (MFA). They can also be incorporated into application delivery controllers (ADC) to improve application security. By safely routing or offloading network traffic, load balancing can help defend against security risks such as distributed denial-of-service (DDoS) attacks.

## Advantages of load balancing
1. Ensure that the application is always available and can scale as needed. Servers can be added or removed based on the number of requests.
2. Prevent a single server from becoming overloaded with requests.
3. Provide encryption, authentication, and other types of additional support.
4. End users only need to know the address of the load balancer, rather than the addresses of every server in the cluster, providing a layer of abstraction.
5. Minimize server response time and maximize throughput.
6. Load balancers can perform health checks and monitor the servers' request-handling capability to ensure proper functioning. They can also be used to roll out software updates without taking the entire service down, by removing one server at a time.

## How a system with a load balancer works
1. The user device sends a request to the DNS server to resolve the domain name.
2. The DNS server maps the domain to the load balancer’s IP address.
3. The DNS server responds to the user device with the load balancer’s IP, hiding backend servers.
4. The user device establishes an HTTPS connection with the load balancer.
5. The load balancer selects a backend server (Server 1, 2, or 3) based on algorithms like round-robin or server load.
6. The load balancer forwards the request to the chosen backend server (e.g., Server 1) using a private IP.
7. The backend server processes the request and generates a response.
8. The backend server sends the response back to the load balancer.
9. The load balancer forwards the response to the user device.
10. The user device receives and displays the response, as if it came directly from the server.

## Load Balancing Algorithms
1. **Round Robin**: Each request is sequentially distributed to the next server in a circular manner.
   
2. **Least Connections**: Directs new requests to the server with the fewest active connections.
   
3. **Weighted Round Robin**: Similar to the Round Robin but there is a weight associated with each server (weight represents the server capacity). So the servers with higher weights receive a larger proportion of the load.
   
4. **Random Load**: The randomized load-balancing algorithm randomly distributes requests to servers using a random number generator. When a load balancer receives a request, randomized algorithm evenly distributes it to the servers.
   
5. **Least Response Time**: Considers the response times of the servers and directs the request to the server with the lowest response time.
   
6. **IP Hash**: Calculates a hash value based on the client's IP address to select the server from the pool. This will ensure that requests from the same client will be directed to the same server.

## Considerations / Concerns
1. Single Point of Failure (SPOF)

    A load balancer itself can become a bottleneck or failure point if not deployed redundantly.
   - **Mitigation**: Use multiple load balancers (e.g., AWS ALB/NLB are managed and highly available by default, but self-managed HAProxy/Nginx need redundancy setup).

2. Latency Overhead

    Every LB hop introduces network latency. In a distributed system with multiple tiers (API LB → service LB → database proxy LB), these latencies add up.
    - **Mitigation**: Minimize unnecessary LB layers; consider direct service discovery

3. Security Considerations
   
    The LB is an exposed entry point → subject to DDoS, SYN floods, and other attacks. TLS termination at the LB means traffic is unencrypted inside the network unless re-encrypted.
    - **Mitigation**: Use WAF (Web Application Firewall), DDoS protection (AWS Shield), and re-encryption if needed.

1. Debugging Complexity
    
    Multiple LB layers obscure traffic flow. Harder to trace issues (is it DNS? LB health check? LB routing policy? Backend failure?).
    - **Mitigation**: Use distributed tracing (X-Ray, OpenTelemetry) and logging at the LB layer.
  
1. Session Persistence (Sticky Sessions) 
    - Normally, a load balancer distributes requests across multiple backend servers using a strategy like round robin or least connections.
    
    - But some applications store session state in memory on a server (e.g., user login data, shopping cart, temporary cache).

    - If the user’s next request gets routed to a different backend server, that new server doesn’t know their session state → leading to logout, missing data, or errors.

    - **Mitigation**: 
      - To fix this, load balancers offer session persistence (stickiness): If clients need “stickiness” (e.g., session data on one server), the LB must track connections. This reduces flexibility in scaling and can cause uneven load distribution.
    
      - Use stateless services + distributed caches (Redis, DynamoDB, etc.) instead of relying on LB stickiness.
  
      - **Stickiness Implementation?**
        - Cookie-based persistence - LB inserts a special cookie (e.g., AWSALB in AWS ALB). All requests with that cookie are routed to the same backend.
        - IP-based persistence - LB uses client’s IP to always route them to the same backend. Problematic behind NAT or mobile networks where IP changes often.


## References
1. https://aws.amazon.com/what-is/load-balancing/
2. https://www.enjoyalgorithms.com/blog/types-of-load-balancing-algorithms
3. https://www.ibm.com/think/topics/load-balancing