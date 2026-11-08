---
title: Chapter 5
---
## Networking Basics

- Router connects a network
- Each machine has a unique IP that is assigned to it - has to be a unique
- IPv4 is 32-bit
- IPv6 is 128 address

## Amazon VPC

- Enables provisioning of logically isolated section AWS cloud where resources can be launched
- Control of own networking resources
  - Selection of IP address range
  - Creation of subnets
  - Configuration of route tables and network gateways
- Customize network configuration of VPC
- Have multiple layers of security

### VPCs and subnets

#### VPCs

- Logically isolated from other VPCs
- Dedicated to AWS account
- Belong to single region - can span many availability zones

### Subnets

- Range of IP addresses dividing a VPC
- Belong to single Availability zone
- Public or private

### IP addressing

- VPCs are assigned IPv4 CIDR block
- Cannot change address range after creation
- Largest block is /16 and smallest is /28
- CIDR blocks can not overlap
- IPv6 is also supported with different block size limit

#### Reserved addresses

| IP address block 10.0.0.0/24 | Reserved for              |
| :--------------------------- | :------------------------ |
| 10.0.0.0                     | Network address           |
| 10.0.0.1                     | Internal communication    |
| 10.0.0.2                     | DNS resolution            |
| 10.0.0.3                     | Future use                |
| 10.0.0.255                   | Network broadcast address |

#### Public IP address types

- Public IPv4 address
  - Manually assigned through Elastic IP address
  - Assigned through auto-assign IP address setting at subnet
- Elastic IP address
  - Associated with AWS account
  - Can be allocated with AWS account
  - Can be allocated and remapped anytime
  - Additional costs might apply

#### Elastic network interface

- Elastic network interface is a virtual network interface that can be attached to an instance or detached, attached to another instance
- Attributes follow when reattached to new instance
- Each instance in VPC has default network interface that is assigned private IP address from VPC range

#### Route tables and routes

- Route table contains set of rules that can configure direct network traffic from subnet
- Route specifies destination and target
- Default- route table contains local route for communication within VPC
- Subnet must be associated with route table (1 at most)

## VPC networking

- NAT gateway - Public route table - Internet gateway - Internet

### VPC peering

- Can connect VPCs in own AWS account, between AWS account, or between AWS regions
- Restrictions
  - IP spaces cannot overlap
  - Transitive peering not supported
  - Can only have one peering resource between same two VPCs

### VPC endpoints

- Two types of endpoints
  - Gateway endpoints (S3 and DynamoDB)
  - Interface endpoints (provided by PrivateLink)

## VPC Security

### Security groups

- Security groups act at the instance level
- Rules are used to manage instance traffic
- Default security groups are sealed shut to inbound traffic. Need to define rules
- Stateful security groups. Outbound traffic always allowed

### Network access control list (ACLs)

- Network ACLs act at subnet level
- Network ACL has separate inbound and outbound rules - either allowing or denying traffic
- Default network ACLs allow all inbound and outbound IPv4 traffic
- Network ACLs are stateless

### Security groups vs network ACLs

| Attribute       | Security Group                                               | Network ACLs                                        |
| --------------- | ------------------------------------------------------------ | --------------------------------------------------- |
| Scope           | Instance level                                               | Subnet level                                        |
| Supported rules | Allow rules only                                             | Allow and deny rules                                |
| State           | Stateful (return traffic automatically allowed, rules ignored) | Stateless (return traffic must be allowed by rules) |
| Order of rules  | Rules are evaluated before allowing traffic                  | Rules evaluated in order before allowing traffic    |

## Amazon Route 53

- Highly available and scalable DNS web service
- Used to route end users to internet applications by translating names to IP addresses
- IPv4/IPv6 
- Connects user requests to infrastructure inside and outside AWS
- **Simple routing:** use in single-server environment
- **Weighted routing:** assign weights to resource record to specify frequency
- **Latency routing-** route traffic based on location of users
- **Geoproximity routing:** Route traffic based on location of resources
- **Failover routing:** failing over to backup site if primary site fails
- **Multivalve answer routing:** respond to DNS queries with 8 healthy records

## Amazon CloudFront

- Global CDN
- Network of edge locations and regional edge caches
- Self-service model
- Pay as

