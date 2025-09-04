# Scaling

Scalability is the property of a system to handle a growing amount of load by adding resources to the system.

## System growth aspects

1. User Base - More users started using the system, leading to increased number of requests.

2. Growth in Features - More features were introduced to expand the system's capabilities.

3. Data Volume - Growth in the amount of data the system stores and manages due to user activity or logging.

4. Complexity - The system's architecture evolves to accommodate new features, scale, or integrations, resulting in additional components and dependencies.

5. Geographic Reach - The system is expanded to serve users in new regions or countries.

## Types of scaling
1. Vertical Scaling (Scale up)

    This means adding more power to your existing machines by upgrading server with more RAM, faster CPUs, or additional storage.

    - Pros:
        - Easier to implement since it involves upgrading existing machines.
        - No need to modify the application architecture.

    - Cons:
        - Limited by the maximum capacity of a single machine.
        - Single point of failure: if the machine goes down, the application becomes unavailable.
  
    - Use Cases: Initial stages of a project, applications with low to moderate growth.

2. Horizontal Scaling (Scale out)

    This means adding more machines to your system to spread the workload across multiple servers.

    It's often considered the most effective way to scale for large systems.

    - Pros:
        - Virtually limitless scalability by adding more machines.
        - Increases redundancy, reducing the risk of a single point of failure.

   - Cons:
      - More complex to implement due to the need for distributed systems design.
      - Requires load balancing and data distribution strategies.

   - Use Cases: High-growth applications, distributed systems, applications requiring high availability.

3. Auto-Scaling
   
    Auto-Scaling means automatically adjusting the number of active servers based on the current load.

    This ensures that the system can handle spikes in traffic without manual intervention

    - Pros:
        - Dynamic scaling based on real-time demand.
        - Cost-efficient as resources are used only when needed.

   - Cons:
        - Requires accurate load prediction and monitoring.
        - Potential for delays in scaling actions, leading to temporary performance issues.
    - Use Cases: Cloud-based applications, unpredictable traffic patterns, cost-sensitive applications.

## References
1. https://www.linkedin.com/pulse/system-design-key-concepts-scalability-saeed-anabtawi--1g0pf/