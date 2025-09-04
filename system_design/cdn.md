# Content Delivery Network (CDN)


A **Content Delivery Network (CDN)** is a system of geographically distributed servers that deliver web content to users based on their location. Instead of relying on a single origin server, a CDN caches copies of your content in multiple **edge servers** located around the globe.  

When a user requests your website, the CDN routes them to the nearest server for **faster, more reliable access**.

## How Does a CDN Work?
1. **User Request**  
   A visitor opens your website. Instead of pulling everything from your origin server, the request goes through the CDN.  

2. **Nearest Edge Server**  
   The CDN finds the closest server (Point of Presence, or **PoP**) to the user.  

3. **Content Delivery**  
   - If the content is cached on the edge server, it is delivered instantly.  
   - If not, the edge server retrieves it from the origin, caches it, and serves it.  


## Benefits of Using a CDN
1. Reduce page load time - Website traffic can decrease if your page load times are too slow. A CDN can reduce bounce rates and increase the time users spend on your site.

2. Reduce bandwidth costs - Bandwidth costs are a significant expense because every incoming website request consumes network bandwidth. Through caching and other optimizations, CDNs can reduce the amount of data an origin server must provide, reducing the costs of hosting for website owners.

3. Increase content availability - Too many visitors at one time or network hardware failures can cause a website to crash. CDN services can handle more web traffic and reduce the load on web servers. Also, if one or more CDN servers go offline, other operational servers can replace them to ensure uninterrupted service.

4. Improve website security - Distributed denial-of-service (DDoS) attacks attempt to take down applications by sending large amounts of fake traffic to the website. CDNs can handle such traffic spikes by distributing the load between several intermediary servers, reducing the impact on the origin server.

## Examples
1. Cloudflare: An e-commerce platform caches images, blocks DDoS attacks, and optimizes pages, reducing load time by 60%.
2. Akamai: A streaming service delivers 4K videos with 50ms latency via local PoPs and dynamic optimization.
3. Amazon CloudFront: A gaming company distributes patches, cutting download times by 80% with HTTPS.
4. Fastly: A news site caches articles and purges caches instantly, maintaining sub-second load times.
5. Microsoft Azure CDN: A corporate site delivers brochures globally, reducing load times by 60% with compression.

## Considerations / Limitations
1. Cache Invalidation / Stale Content
   
   CDNs cache content at edge locations to reduce origin load and latency. Updating content on the origin doesn’t automatically update the cache. Users may see stale data.

   - **Mitigation**:
      - Use short cache TTLs for dynamic content.
      - Purge/invalidate cache when content changes.
  
2. Dynamic Content / Personalization
   
   CDNs work best with static content (images, JS, CSS, videos). For dynamic, user-specific content, caching is tricky -- Personalized pages may bypass the CDN → higher origin load.

3. Consistency & Cache Propagation

   Global CDNs may have multiple edge nodes. Propagating updates to all nodes may take seconds to minutes, depending on provider.
   - **Mitigation**: Plan cache invalidation carefully and design for eventual consistency.

4. Request Routing & Latency

   CDNs route requests to the nearest edge location. In some cases, the nearest edge may not be the fastest path due to network issues. 
   
   Certain regions may have fewer PoPs, causing higher latency.

## References
1. https://www.akamai.com/glossary/what-is-a-cdn
2. https://aws.amazon.com/what-is/cdn/
3. https://www.cloudflare.com/learning/cdn/what-is-a-cdn/
4. https://medium.com/@joudwawad/aws-cloudfront-deep-dive-08bd04081662
5. https://medium.com/@roopa.kushtagi/a-z-of-content-delivery-networks-cdn-making-the-internet-faster-and-more-reliable-57786b46a058
6. https://www.designgurus.io/blog/content-delivery-network-cdn-system-design-basics
7. https://blog.algomaster.io/p/content-delivery-networks
8. https://www.f5.com/glossary/content-delivery-network-cdn