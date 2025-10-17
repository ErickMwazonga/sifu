# Blog Storage

## Object Storage (BLOB)?
Object Storage is a special type of storage designed to handle massive amounts of unstructured data. These could be images, videos, or other files.

## Blog key aspects
1. Data: The actual binary content that you’re storing.
2. Unique Identifier: The object’s address within the storage system.
3. Metadata: Information about the object (filename, type, size, creation date, etc.)

## Features
1. **Durability**: Blob storage services are designed to be incredibly durable. They use techniques like replication and erasure coding to ensure that your data is safe even if a disk or server fails.

2. **Scalability**: Hosted blob storage solutions like AWS S3 can be considered infinitely scalable. They can store an unlimited amount of data and can handle an unlimited number of requests (obviously within the limits of your account). 

3. **Cost**: Blob storage services are designed to be cost effective. They are much cheaper than storing large blobs of data in a traditional database. 
   
4. Storage Classes / Tiers
5. Replication - Cross-region or cross-zone replication which is useful for disaster recovery and geo-distribution.

6. **Security**: Blob storage services have built-in security features like encryption at rest and in transit. They also have access control features that allow you to control who can access your data.

7. **Upload and Download Directly from the Client**: Blob storage services allow you to upload and download blobs directly from the client. This is useful for applications that need to store and retrieve large blobs of data, like images or videos. 

8. Versioning

   With bucket versioning, we can store multiple versions of the same object in a bucket, and restore them - this prevents accidental deletes or overwrites. To some extent, versioning also lets us work around the immutability of the write-ahead log.
   
9.  Chunking / Multipart uploads
   
   With multipart uploads, we can upload objects in smaller parts, either sequentially or in parallel, and after all parts are uploaded, we reassemble the object from its parts. This is useful for large uploads (e.g. videos) that may take long and so are at risk of failing mid-upload. On upload failure, the client resumes from the last successfully uploaded part, instead of having to start over from the beginning. What could this look like?

## Use cases
1. Media: Image, video, and audio data take up a lot of space, and sometimes needs to be stored but not necessarily accessed regularly.
   
2. Logs
   As software executes, it constantly creates a series of events that can be recorded in logs for later analysis. The volume of this data can increase quickly. Blob storage enables quick and cheap storage of this data in an unstructured form. However, blob storage is less cost-effective for this use case. Any query of log data will cost egress fees.
   
3. Backups and disaster recovery:
   
   Most organizations need to keep complete backups, particularly for recovering from ransomware attacks. As this data is duplicated in production and rarely accessed, blob storage is well-suited for backing up large data sets.

## Pre-signed urls

Pre-signed URLs are commonly used when you want temporary, controlled access to private files stored in a service like Amazon S3.

### Why pre-signed URLs
1. Secure access to private files - By default, objects in S3 (or other storage) are private. A pre-signed URL lets you give someone access to a file without making it public.

2. Time-limited access - The URL has an expiration time (e.g., 5 minutes, 1 hour). After that, it becomes invalid, so the person can’t keep downloading/uploading forever.

3. Granular permissions - You can generate a pre-signed URL for download (GET) or upload (PUT/POST) without exposing your AWS credentials.

    > Example: A client can upload a file directly to S3 with a pre-signed URL, but they don’t get full S3 access.

4. Offloading traffic from your servers - Instead of your backend receiving large files and then uploading them to S3, you just hand the client a pre-signed URL. They upload/download directly with S3, saving your server bandwidth and costs.

5. Auditing and control - Since each URL is generated on demand and has an expiry, you have better control and can log who requested it.

### How it works
1. Upload
   - When clients want to upload a file, they request a presigned URL from the server.
   - The server returns a presigned URL to the client, recording it in the database.
   - The client uploads the file to the presigned URL.
   - The blob storage triggers a notification to the server that the upload is complete and the status is updated.

2. Download
   - The client requests a specific file from the server and are returned a presigned URL.
   - The client uses the presigned URL to download the file via the CDN, which proxies the request to the underlying blob storage.

### Common Issues with Pre-signed URLs
1. Exposure if leaked - If someone gets hold of the URL while it’s valid, they can use it.  
    - **Example:** A user shares a download link with someone who wasn’t supposed to have access.  
  
    - **Mitigation:** Keep expiry times short, generate just-in-time, and optionally restrict by IP or content-type.

2. No built-in access revocation - Once a pre-signed URL is generated, you can’t revoke it until it expires. If you accidentally shared it or need to revoke access, you’re stuck unless you change the object itself (rename/move/delete).  

    - **Mitigation:** Use very short expirations and regenerate URLs when needed.

3. Limited control & auditing - You can’t easily track who used the pre-signed URL unless you build extra logging. It doesn’t carry user identity information — it’s just a signed link.  

    - **Mitigation:** Log usage via CloudTrail/S3 access logs, or proxy requests through your backend if you need full auditing.

4. Potential for misuse in uploads - If you give a client a pre-signed **PUT/POST URL**, they can upload any content (malicious files, oversized files, wrong types).  

    - **Mitigation:** Add constraints (e.g., max file size, content-type) when generating the URL, and validate after upload.

5. Tight coupling with object keys - A pre-signed URL gives access to a **specific object key**. If keys are predictable (e.g., `user123/profile.png`), a malicious user might overwrite another user’s files.  

    - **Mitigation:** Use unique, random object keys and enforce object ownership on the backend.

6. Scaling challenges - If every request requires generating a fresh pre-signed URL, it can add backend load.  

    - **Mitigation:** Cache or batch URL generation, or only generate on-demand.

7. Expiration mismatch with client use - If a client doesn’t use the URL before it expires (e.g., due to network issues), the operation will fail.  

    - **Mitigation:** Handle retries gracefully by requesting a new pre-signed URL.

## Multi-part upload with S3

1. Initiate Multipart Upload
    
    - Client calls `CreateMultipartUpload` with bucket, file key, and optional metadata.
    - S3 returns an `UploadId` to identify this upload session.

2. Split File into Parts

    - Client divides the file into chunks (typically 5 MB–5 GB each).
    - Each chunk is assigned a part number (starting at 1).

3. Upload Each Part

    - Client uploads each chunk via `UploadPart` with `UploadId` and `PartNumber`.
    - S3 returns an `ETag` for each uploaded part.
    - Client tracks `PartNumber` → `ETag` mapping.
    - Failed parts can be retried individually without restarting the whole upload.

4. Complete Multipart Upload

    - Client calls `CompleteMultipartUpload` with all part numbers and `ETags`.
    - S3 validates the parts and assembles the final object.

5. Verify Success

    - Client confirms upload by:
        - Checking S3’s response from `CompleteMultipartUpload` (includes object ETag and location), or
        - Using HeadObject to ensure object exists, size matches, and optionally verifying checksum.

6. Abort Multipart Upload (Optional)
    - If the upload is canceled or fails irrecoverably, client calls AbortMultipartUpload.

    - S3 deletes all uploaded parts associated with the UploadId.

## Examples
1. Amazon S3 - S3 is a Simple Storage Service that is used for storing large files and retrieving them quickly.

2. Google Cloud Storage  -  Google Cloud offers its object storage service called Google Cloud Storage.

3. Azure Blob Storage  -  Azure also provides a service called Azure Blob Storage.

## References
1. https://medium.com/@tahir.rauf/system-design-dropbox-35cc80ff3e79
2. https://ivov.dev/notes/s3-object-storage
3. https://fourtheorem.com/the-illustrated-guide-to-s3-pre-signed-urls/