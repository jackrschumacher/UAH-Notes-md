---
title: Module 8
---
## Amazon RDS

- Unmanaged: Scaling, fault tolerance, and availability are managed by you
- Managed: Scaling, fault tolerance, availability typically built into the service
- Challenges of relational databases:
  - Server maintenance and energy footprint
  - Software installation and patches
  - Database backups and high availability
  - Limits on scalability
  - Data security
  - OS installation and patches
- You manage:
  - Application optimization
- AWS manages:
  - OS installation and patches
  - Database software installation and patches
  - Database backups
  - High availability
  - Scaling
  - Power and racking/stacking servers
  - Server maintenance

### Amazon RDS DB instances

- DB instance class
  - CPU
  - Memory
  - Network performance
- DB instance storage
  - Magnetic
  - General purpose (SSD)
  - Provisioned IOPS

### Amazon RDS read replicas

- Features
  - Offers asynchronous replication
  - Can be prompted to master if needed
- Functionality
  - Use for read-heavy workloads
  - Offload read queries

- Use cases
  - High-throughput
  - Storage scalability
  - Low-cost database
  - Fully managed solution
  - Rapidly grow capacity
- Clock-hour billing:
  - Resources incur charges when running
  - Database characteristics: 
    - Physical capacity of database
      - Engine 
      - Size
      - Memory class
- DB purchase types
  - On demand instances
    - Compute by the hour
  - Reserved instances
    - Low, one-time, upfront payment for database instance that are reserved with 1 or 3 year term
  - Charged by GB/Month
- Requests
  - Number of input and output requests made to database
- Deployment type - single vs multiple availability zones
- Data transfer
  - No charge for inbound data transfer
  - Tiered charges for outbound data transfer

## Amazon DynamoDB

|              | Relational       | Non-Relational                     |
| ------------ | ---------------- | ---------------------------------- |
| Data Storage | Rows and Columns | Key-value, document, graph         |
| Schemas      | Fixed            | Dynamic                            |
| Querying     | Uses SQL         | Focuses on collection of documents |
| Scalability  | Vertical         | Horizontal                         |

- Fast and flexible NoSQL database service for any scale
  - No SQL database tables
  - Virtually unlimited storage
  - Items can have differing attributes
  - Low-latency queries
  - Scalable read/write output
- Tables, items and attributes are core DynamoDB components
- DynamoDB supports two different kinds of primary keys: Partition key and partition and sort key

## Amazon Redshift

- Analytics is an important part of business today
- Enterprise data warehouse
  - Migrate at a pace customers are comfortable with
  - Experiment without large upfront or commitment
  - Respond faster to business needs
- Big data
  - Low price point for small customers
  - Managed service for ease of deployment and maintenance
  - Focus more on data and less on database management
- Software as a service
  - Scale data warehouse capacity as demand grows
  - Add analytic functionality to applications
  - Reduce HW and SW costs

## Amazon Aurora

- Enterprise-class relational database
- Compatible with MySQL or PostgreSQL
- Automate time-consuming tasks (such as provisioning, patching, backup, recovery,etc)