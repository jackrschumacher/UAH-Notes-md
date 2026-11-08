---
title: Chapter 6
---
## Compute Services overview

- Amazon EC2 
  - Infrastructure as a service
  - Instance based
  - Virtual machines
  - Provision VMs that you can manage as you choose
- AWS Lambda
  - Serverless computing
  - Function based
  - Low-cost
  - Write and deploy code that can be trigged by events
  - Use when possible
- Amazon ECS / Amazon EKS / AWS Fargate / Amazon ECR
  - Container based computing
  - Instance based
  - Spin up and execute jobs more quickly
  - Reduce administrative overhead
- AWS Elastic Beanstalk
  - Platform as a service
  - For web applications
  - Focus on code
  - Can easily tie into other services - databases, DNS, etc.
- Optimal compute service or service that you use will depend your use
- Application design, usage patterns, configuration settings

## Amazon EC2

- Choices made using Launch instance wizard:
  - AMI
    - Template used to create EC2 instance
    - Contains Windows or Linux OS
    - Software pre-installed
  - Instance Type
    - First letter is the family name
    - Second value is generation number
    - Everything after the period is the size
  - Network settings
    - Varies by instance type
    - Maximize by putting in cluster placement group
    - Enable enhanced networking
    - Where should it be deployed? 
      - VPC and optional subnet
      - Should a public IP be automatically assigned
  - IAM role
    - What software on the EC2 instance needs to interact with other AWS services - attach an IAM role if needed
    - IAM roles are kept in an instance profile
    - Not restricted to attaching a role only at instance launch
  - User data
    - Can specify a script to run at launch
    - Can customize the runtime environment - script executes the first time the instance starts
    - Can be used to reduce number of custom AMIs that are needed to be maintained
  - Storage options
    - Configure root volume and optionally attach additional storage 
    - Specify size of the disk, volume time, what will happen if the instance is deleted, if encryption should be used
    - Amazon Elastic Block store
      - Block-level, durable
      - Can stop instance and start instance and data is retained
    - Amazon EC2 Instance store
      - Storage provided on disks attached to host computer where EC2 is running
      - Data stored is deleted if the instance is stopped
    - Can mount Amazon EFS or Amazon S3
  - Tags
    - Label that can be assigned to AWS resource
    - Can attach metadata to EC2 instance
    - Allows filtering, automation, cost allocation, access control
  - Security group
    - Set of firewall rules that control traffic to instance 
    - Create rules that specify the source and which ports that network communications can use
      - Specify port number and protocol such as TCP and UDP or ICMP
      - Specify source (allowed IP address or another security group)
  - Key Pair
    - Specify existing key pair or create new key pair
      - Consists of Public Key that AWS stores
      - Private key is stored by you
    - Enables secure connection to instance
    - Linux - use SSH
    - Windows - use AMI
- EC2 instance can also be created in AWS CLI
- Elastic IP address
  - Rebooting instance does not change IP
  - When instance is stopped and started, public IP and external DNS hostname will change
  - If required a persistent public IP address, associate elastic IP with instance
    - Can be associated with instance in region as needed
    - Remains allocated to account until you choose to release
- EC2 instance metadata
  - Data about instance
- Cloud Watch for Monitoring
  - Basic - 5 min interval
  - Detailed - 1 min interval

### Cost optimization

#### EC2 Pricing models

- On Demand instances
  - Pay by hour
  - No long-term commitments
  - In free tier
- Reserved instances
  - Full, Partial, no upfront payment
  - 1/3 year term
- Spot Instances
  - Run as long as they are available and bid is above spot instance price
  - Can be interrupted by AWS w/ 2 min notification
    - Terminated, stopped, hibernated
  - Can be less expensive compared to on demand
  - Flexibility
- Dedicated Hosts
  - Physical server with EC2 instance completely dedicated to use
- Scheduled Reserved instances
  - Purchased capacity reservation available on reoccurring schedule

- Dedicated instances
  - Run in VPC on HW dedicated to a single customer

#### 4 pillars of cost optimization

- Right Size
  - Provision instances to match need
  - Use metrics
  - Right size, reserve
- Increase elasticity
  - Stop or hibernate EBS instances not in use
  - Use automatic scaling to match needs based on usage
- Optimal pricing model
  - Leverage pricing model for use case
  - Optimize and combine purchase types
  - Consider serverless solutions
- Optimize storage choices
  - Reduce costs while maintaining storage performance and avaliability
  - Resize EBS
  - Change EBS types to lessen storage costs
  - Delete snapshots that are not used

#### Workloads

- Spiky Workloads
  - On-Demand
- Time-sensitive
  - Spot instances
- Steady-state
  - Reserved instances
- Highly sensitive workloads
  - Dedicated hosts

### Measure, monitor and improve

- Cost optimization is an ongoing process
- Recommendations
  - Define and enforce cost allocation tagging
  - Define metrics, target, review
  - Architect for cost
  - Assign responsibility of optimization to individual or team

## Container Services

- Method of OS virtualization
- Repeatable, self contained
- SW runs the same in different enviroments
- Faster to launch and stop or terminate than virtual machines

### Docker

- SW platform that allows for building, test, run quickly
- Run containers on docker
- Containers has what is needed for an app to run

### Kubernetes

- OSS for container orchestration
  - Deploy and manage containerized apps at scale
  - Can be used on prem and in cloud
- Complements Docker
  - Enables to run multiple containers on single host OS
  - Orchestrates many docker hosts
- Automates
  - Container provisioning
  - Networking
  - Load distribution
  - Scaling

### Amazon EKS

- Enables you to run Kubernetes on AWS
- Certified Kubernetes conformat (migration is easy)
- Compatible with community tools
- Manage clusters of EC2 compute instances
- Containers orchestrated by Kubernetes can run

## AWS Lambda

- Serverless compute
- Supports many languages
- Pay-per-use
- Supports orchestration of multiple functions

## AWS Elastic Beanstalk

- Easy way to get web apps running on AWS
- Deployment, load balancing, health monitoring,etc.
- Auto deployment,etc.
- No additional charge
- Only pay for resource usage
- Select optimal resources 