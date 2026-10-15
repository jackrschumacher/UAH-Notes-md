---
title: Chapter 3
---
## AWS Global Infrastructure

- Designed to be flexible, reliable, scalable and secure infrastructure 

### AWS regions

- Geographical region
  - Data replication across regions controlled by user
  - Communication between regions uses AWS network infrastructure
- Full redundancy and connectivity to network
- Usually has 2+ availability zones
- Some regions might have restricted access depending on country

#### Selecting a region

Factors:

- Data governance
- Proximity to Customers (Latency)
- Services available within the region
- Costs (varying by region)

#### Availability zones

- Regions have multiple availability zones 
- Each availability zones is fully isolated partition of AWS infrastructure
  - Discrete data centers
  - Designed for fault isolation
  - User chooses availability zones 
  - Isolated and protected from events (within reason)

#### AWS data centers

- Designed for security
- Each data center has redundant power, networking, connectivity. Each is housed in separate facility
- 50,000-80,000+ servers per center
- Data center locations are not disclosed

#### Points of Prescence

- 187 points of Prescence
  - 176 edge locations
  - 11 Regional edge cache
- Used with Amazon CloudFront
  - Reduced latency CDN
- Regional edge for content with infrequent access

#### AWS infrastructure features

- Elasticity and scalability
  - Elastic infrastructure, dynamic adaption 
  - Scalable infrastructure
- Fault-tolerance
  - Continues operating even if a failure occurs
  - Redundancy of components
- High availability
  - High-level operational performance
  - Minimize downtime
  - No human intervention

### AWS Services

- Three parts
  - Platform services
  - Foundation services
  - Infrastructure
- 23 product categories, each category with 1+ services

#### Storage services

- S3
- Amazon Elastic Block Store (EBS)
- Amazon Elastic File System (EFS)
- Amazon Simple Storage Glacier

#### Compute services

- Amazon EC2
- Amazon EC2 auto-scaling
- Amazon Elastic Container Service (ECS)
- Amazon EC2 Container registry
- AWS Elastic beanstalk
- AWS Lambda
- Amazon Elastic Kubernetes Service (EKS)
- AWS Fargate - compute engine for Amazon ECS

#### Database service

- Amazon Relational Database service
- Amazon Aurora
- Amazon Redshift
- Amazon Dynamo DB

#### Networking and content delivery

- Amazon VPC
- Elastic Load Balancing
- Amazon Cloud Front
- AWS Transit Gateway
- Amazon Route 53
- AWS Direct Connect
- AWS VPN

#### Security, identity and compliance

- AWS Identity and Access management (IAM)
- AWS Organizations
- Amazon Cognito
- AWS artifact
- AWS Key Management service
- AWS Shield

#### AWS cost management

- AWS cost and usage report
- AWS Budgets
- AWS Cost explorer

#### AWS management and governance 

- AWS Management console
- AWS Config
- Amazon CloudWatch
- AWS AutoScaling
- AWS CLI
- AWS Trusted Advisor
- AWS Well-architected tool
- AWS CloudTrail