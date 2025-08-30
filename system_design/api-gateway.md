# API Gateways

## Introduction to API Gateways

An API Gateway acts as a reverse proxy between clients (e.g., web browsers, mobile apps, or external systems) and backend services (e.g., microservices, databases, or legacy systems). It serves as a centralized entry point for managing, routing, and securing API requests. 

Imagine it as a postman who delivers mail to the correct house, checks the sender's identity, manages delivery schedules, and even translates letters when needed.

## Core Features of an API Gateway

### 1. Authentication and Authorization

**Description**:  
The API Gateway centralizes authentication (verifying user identity) and authorization (ensuring permission to access resources), eliminating the need for each microservice to handle these independently.

**How It Works**:  
- Validates tokens (e.g., OAuth2, JWT) or API keys.
- Integrates with identity providers like Okta or Auth0.
- Enforces role-based or attribute-based access control before forwarding requests.

**Example**:  
A mobile app sends a request with a JWT token. The gateway verifies the token and checks if the user has the "admin" role before routing the request to an admin-only service.

---

### 2. Request Routing

**Description**:  
The API Gateway directs incoming requests to the appropriate backend service based on URL paths, HTTP methods, or headers, abstracting the complexity of microservice architecture.

**How It Works**:  
- Maps endpoints (e.g., `/users`) to specific services.
- Supports load balancing across multiple service instances.

**Example**:  
A request to `/api/users` routes to the User Service, while `/api/orders` routes to the Order Service.

---

### 3. Rate Limiting and Throttling

**Description**:  
Rate limiting protects backend services from excessive requests by enforcing quotas, preventing overload and ensuring fair usage.

**How It Works**:  
- Limits requests per client (e.g., 100 requests per minute).
- Returns HTTP 429 (Too Many Requests) when limits are exceeded.

**Example**:  
A public API allows 100 requests per minute for free-tier users, blocking excess requests to maintain service stability.

---

### 4. Monitoring and Analytics

**Description**:  
The API Gateway collects metrics and logs for API traffic, enabling performance monitoring, error tracking, and usage analytics.

**How It Works**:  
- Logs request/response details like latency, status codes, and error rates.
- Integrates with tools like Prometheus, Grafana, or AWS CloudWatch.

**Example**:  
Tracking latency for `/api/orders` to identify and optimize slow services.

---

### 5. Request/Response Transformation

**Description**:  
The gateway modifies requests or responses, such as adding headers, transforming data formats, or filtering sensitive information.

**How It Works**:  
- Adds headers like `X-API-Version`.
- Converts JSON to XML for legacy clients.
- Filters sensitive data (e.g., passwords) from responses.

**Example**:  
A legacy client requires XML, but the backend returns JSON. The gateway transforms the response to XML.

---

### 6. Protocol Translation

**Description**:  
The API Gateway converts between protocols (e.g., HTTP to gRPC) or data formats (e.g., JSON to XML) to ensure compatibility between clients and services.

**How It Works**:  
- Translates RESTful HTTP requests to gRPC for modern services.
- Converts data formats for legacy systems.

**Example**:  
A client sends an HTTP request, but the backend uses gRPC. The gateway handles the protocol conversion.

---

### 7. Caching

**Description**:  
The API Gateway caches responses to reduce latency and offload backend services, improving performance for frequently requested data.

**How It Works**:  
- Stores responses in memory (e.g., Redis) based on cache keys (e.g., URL or query parameters).
- Sets cache expiration policies (e.g., TTL of 60 seconds).

**Example**:  
Caching the response of a product catalog API to serve repeated requests without querying the backend.

---

### 8. Service Orchestration

**Description**:  
The gateway aggregates responses from multiple services into a single response, simplifying client interactions with complex microservice architectures.

**How It Works**:  
- Combines data from multiple backend services.
- Handles sequential or parallel calls to services.

**Example**:  
A client requests user profile data, which requires combining data from the User Service (name, email) and Order Service (recent orders).

---

### 9. Security Enforcement

**Description**:  
The API Gateway enforces security measures like input validation, DDoS protection, and encryption to protect backend services.

**How It Works**:  
- Validates request payloads against schemas.
- Mitigates DDoS attacks using rate limiting and IP filtering.
- Enforces HTTPS for secure communication.

**Example**:  
Blocking a request with an invalid JSON payload or rejecting requests from a suspicious IP address.

---
### 10. Request Validation
Description:
Ensures incoming requests meet predefined criteria (e.g., schema, format, or required fields) before forwarding to backend services, enhancing security and reliability.
How It Works:

Validates request payloads against JSON or XML schemas.
Checks for required headers, query parameters, or body fields.
Rejects invalid requests with appropriate error messages (e.g., HTTP 400 Bad Request).

Example:
An e-commerce API at /api/orders/create requires a JSON payload with mandatory fields like userId, items, and total. The API Gateway validates the payload against a schema, rejecting requests missing any field.


## Benefits of an API Gateway

1. **Single Access Point**:  
   Simplifies client interactions by providing one entry point for all API requests, reducing the need to manage multiple service endpoints.

2. **Protects Backend Services**:  
   Centralizes security features like authentication, rate limiting, and input validation, shielding services from unauthorized access or attacks.

3. **Simplifies Client-Side Interaction**:  
   Abstracts the complexity of microservices, allowing clients to interact with a unified API without worrying about backend architecture.

4. **Improves Performance**:  
   Features like caching and load balancing reduce latency and optimize resource usage.

5. **Enhances Scalability**:  
   Service orchestration and protocol translation enable seamless integration of diverse services, supporting system growth.

## Examples
1. AWS API Gateway
2. Apigee (Google Cloud)
3. Microsoft Azure API Management
4. Kong - An open-source API Gateway and platform known for its flexibility and plugin-based architecture.

## Considerations / Limitations
1. Throttling & Limits

   By default, API Gateway applies 10,000 requests per second (RPS) soft limit per account per region.

   Burst capacity (concurrent requests) is also limited.

   - **Mitigation**: Request limit increases, implement client-side retries with backoff, and use SQS/Kinesis to smooth spikes.
  
2. Payload & Protocol Limits

   Max payload size: 10 MB for REST APIs and HTTP APIs (WebSocket API = 128 KB).

   Doesn’t support streaming large files directly.

   - **Mitigation**: For large file uploads/downloads, use S3 pre-signed URLs instead of going through API Gateway.

## Questions
1. API Gateway vs LB - Which comes first?
   - https://medium.com/@sandeepsharmaster/architecture-essentials-pairing-api-gateways-with-load-balancers-325e80ca38e5
   - https://stackoverflow.com/questions/61174839/load-balancer-and-api-gateway-confusion

## References
1. https://medium.com/@joudwawad/aws-api-gateway-deep-dive-rest-apis-5ae16a326b3a
2. https://www.hellointerview.com/learn/system-design/deep-dives/api-gateway