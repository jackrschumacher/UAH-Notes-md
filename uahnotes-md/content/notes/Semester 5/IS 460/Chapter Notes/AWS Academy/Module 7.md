---
title: Chapter 7
---
## AWS EBS

### Introduction

- Amazon Elastic Block store- used with EC2 instances
- Non-volatile storage
- Designed for high-availability
- Block storage only changes one block of information in the file, not the whole file itself 
- Enables creation of individual storage volumes and attach them to EC2 instance
  - Offers block-level storage
  - Volumes replicated within availability zones
  - Can be backed up to S3 through Snapshots
  - Ex: boot volume storage, data storage in a file system, database hosts, enterprise applications
- Snapshots
  - Print in time snapshots
  - Recreate new volume at any time
- Encryption
  - Encrypted AWS EBS volumes
  - No cost
- Elasticity
  - Increase capacity
  - Change to different types

### Volumes, IOPS, Pricing

- Volumes
  - Persist independently from the instance
  - All volume types are charged by amount provisioned per month
- IOPS
  - General-purpose SSD- charged by amount provisioned in GB/month
    - Volume types charged by amount provisioned per month
  - Magnetic
    - Charged by number of requests to volume
  - Provisioned IOPS SSD
    - Charged by amount provisioned in IOPS (multiplied by percent of days provisioned per month)

## Amazon S3 (Simple Storage Service)

- Data is stored as objects in buckets
- Virtually unlimited storage - 5 TB object upload limit
- Designed for 11 9s of durability
- Granular access to buckets and objects
- Storage classes:
  - S3 standard
  - S3 Intelligent-tiering
  - S3 Standard-Infrequent Access
  - S3 One Zone-Infrequent Access
  - Amazon S3 Glacier
  - S3 Glacier Deep Archive
- Designed to be easily scaled
- Access Data from management console, CLI, or SDK
- Backup and storage, application hosting, media hosting
- Paying only for what you use
  - Transfers into S3 are not charged
  - S3 transfers out to amazon services in the same region
- GET Retrieves an Object from S3



### Amazon S3 Glacier

- Data archiving service designed for long term data storage
- Supports encryption of data in transit
- Low-cost- best for long-term archiving
- Can configure lifecycle for archiving content
  - Enable deletion or movement of objects based on object age
- Various retrieval speed options that have different price points
- Can be used with REST, Java, .NET SDK, Amazon 
- Can control access via IAM
- S3 Glacier manages keys for you

#### S3 storage classes

- S3 Standard
  - 3+ availability zones
- S3 Standard-infrequent access
  - Retrieval fee with objects
  - Suitable for infrequently accessed data
- S3 Intelligent-Tiering
  - Automatically moves objects between S3 tiers based on access patterns
- S3 One-zone IA
  - One availability zone
  - Costs lest than Amazon S3 standard IA
- S3 Glacier
  - Not-available for real time access
  - Must resotre objects before access
  - Restoring objects takes between 1 min-12 hours
- S3 Glacier deep archive
  - Lowest cost storage for long-term retention 
  - 3+ availability zones
  - Retrieval time within 12 hours

| Item              | Amazon S3                  | Amazon S3 Glacier    |
| ----------------- | -------------------------- | -------------------- |
| Data Volume       | No limit                   | No limit             |
| Average latency   | Milliseconds               | minutes/hours        |
| Item size         | 5 TB max                   | 40 TB max            |
| Cost/GB/Month     | Higher                     | Lower                |
| Billed Requests   | PUT, COPY, POST, LIST, GET | Upload and Retrieval |
| Retrieval pricing | Cents/request              | More cents/request   |



## Amazon Elastic File System (Amazon EFS)

- File storage in AWS Cloud
- Works well for big data, analytics, media processing, content management, web serving, home directories
- Petabyte-scale, low latency
- Shared storage
- Elastic capacity
- Supports NFS 4.0/4.1
- Compatible with all Linux-based Amazon EC2 images
- No minimum fee or setup costs, pay for what is used
- EFS resources:
  - Mount target
    - Subnet ID
    - Security groups
    - One or more per FS
    - Create in VPC subnet
    - One per availability zone
    - Must be in same VPC
  - Tags
    - Key-value pairs

