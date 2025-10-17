# API Design

## API Protocols
1. REST (Representational State Transfer)
   
    REST uses standard HTTP methods (GET, POST, PUT, DELETE) to manipulate resources identified by URLs. For standard CRUD operations in web and mobile applications, REST maps naturally to your database operations and HTTP semantics, making it the go-to protocol for most web services. This should be your default choice.

2. GraphQL

    GraphQL uses a single endpoint with a query language that lets clients specify exactly what data they need. Think about a mobile app that needs only basic user information versus a web dashboard that displays comprehensive analytics - with REST, you'd either create multiple endpoints or force clients to fetch more data than they need, but GraphQL lets each client request exactly what it needs in a single query.

3. RPC (Remote Procedure Call)
    
    RPC protocols like gRPC use binary serialization and HTTP/2 for efficient communication between services. While REST treats everything as resources, RPC lets you think in terms of actions and procedures - when your user service needs to quickly validate permissions with your auth service, an RPC call like checkPermission(userId, resource) is more natural than trying to model this as a REST resource. It's suitable for microservices or internal APIs, consider RPC for those high-performance connections. Use RPC when performance is critical (see Networking Essentials for deeper protocol details).

## API Patterns

### Versioning
APIs evolve over time, and you need a strategy for handling changes without breaking existing clients. This is particularly important for public APIs where you can't control when clients update their code.

1. **URI Versioning**: Include the version in the URL (e.g., /v1/users).

2. **Header Versioning**: Specify the version in request headers (e.g., Accept: application/vnd.api.v1+json).

3. **Query Parameter Versioning**: Use a query parameter (e.g., /users?version=1).

> Importance: Versioning prevents breaking changes for existing clients, supports gradual migration, and maintains a good developer experience. For example, when deprecating an API version, I provided a six-month transition period with clear documentation and migration guides to minimize disruption.

### Rate Limiting and Throttling
Rate limiting prevents abuse by restricting how many requests a client can make in a given time period. This protects your system from both malicious attacks and accidental overuse.

Common strategies:
- Per-user limits: 1000 requests per hour per authenticated user
- Per-IP limits: 100 requests per hour for unauthenticated requests
- Endpoint-specific limits: 10 booking attempts per minute to prevent ticket scalping

> You typically implement rate limiting at the API gateway level or using middleware in your application. When limits are exceeded, return a 429 Too Many Requests status code.

### Pagination
When you're dealing with large datasets, you can't return everything at once. Instead, you need pagination to break large result sets into manageable chunks. There are two main approaches to pagination: offset-based and cursor-based.

Common strategies:

1. Offset-based Pagination 

    Offset-based pagination is the simplest approach and used by most websites. You specify how many records to skip and how many to return: `/events?offset=20&limit=10 get`s records 21-30. This is intuitive and easy to implement, but it has problems with large datasets. If someone adds a new event while you're paginating through results, you might see duplicates or miss records as the data shifts.

2. Cursor-based Pagination

    Cursor-based pagination solves this by using a pointer to a specific record instead of counting from the beginning. Here's how it works in practice:

    First request: `/events?limit=10`
    Response includes the events plus a cursor pointing to the last record:
    ```
    {
        "events": [...],
        "next_cursor": "cmd9atj3p000007ky19w1dpy2"
    }
    ```
    Next request: /events?cursor=cmd9atj3p000007ky19w1dpy2&limit=10

### Authentication and Authorization

**Authentication**
- Authentication is the process of verifying the identity of the client or user, typically through credentials like usernames, passwords, API keys, or JSON Web Tokens (JWT).
    > Authentication verifies identity - proving the user is who they claim to be.

- **Authentication: API Keys vs JWT Tokens**
    1. API Keys

        API keys are long, randomly generated strings that act like passwords for applications rather than humans. When a client makes a request, they include their API key in the Authorization header, and your server looks up that key to identify which application is making the request.

    2. JWT (JSON Web Tokens)

        - JWT tokens encode user information directly into the token itself rather than storing session state on your server. When a user logs in successfully, your server creates a JWT containing their **user ID, permissions, and an expiration time**, then signs the entire token with a secret key.

        - Conveniently, when that JWT comes back with future requests, you can verify it's authentic by checking the signature, and you can read the user information directly from the token without any database lookups. The token itself carries all the context you need to authorize the request.

**Authorization**
- Authorization is the process of determining whether an authenticated client or user has the necessary permissions to access or perform certain operations within the API.
    > Authorization verifies permissions - checking if that authenticated user is allowed to perform the specific action they're requesting.
  
- **Authorization: Role-Based Access Control (RBAC)**
  
    Real systems have different types of users with different permissions. RBAC assigns roles to users and permissions to roles:

### Idempotency and retries
TBA

## References
1. https://www.hellointerview.com/learn/system-design/core-concepts/api-design
2. https://www.seangoedecke.com/good-api-design/