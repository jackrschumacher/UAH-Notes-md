---
title: Chapter 4
---
## Introduction

- Security of data is critical
- Must design AWS usage with security in mind

## AWS shared responsibility model

- AWS is responsible for Software and Hardware and AWS Global infrastructure
- Customer is responsible for data, platform, applications, OS, etc.

### AWS responsibility

- AWS is responsible for the infrastructure security
  - Physical security of data centers
  - Hardware and software infrastructure
  - Network infrastructure
  - Virtualization infrastructure

### Customer responsibility

- Customer responsibilities:
  - Amazon Elastic Compute cloud
    - Include patching, maintenance
  - Applications
    - Passwords, role based access,etc.
  - Security group configuration
  - Network configuration
  - Account management
    - Login and permission settings per user

### Service characteristics and service responsibility

- Infrastructure as a Service (IaaS):
  - Customer has more flexibility over configuring network and storage 
  - Responsible for managing more aspects of security
  - Configures access controls
- Platform as a service (PaaS)
  - Customer does not need to manage underlying infrastructure
  - AWS handles OS, DB patching, firewall, disaster recover
  - Focus on code or data
- Software as a service (SaaS)
  - Software centrally hosted
  - Licensed on subscription model or pay as you go
  - Typically accessed via web browser, mobile app, API
  - Do not need to manage infrastructure to support service

## AWS IAM

- Use IAM to access AWS resources
- Resource is something in AWS you can work with
- Example: Control who can back up to an AWS S3 connection work
- Define fine grained access rights
  - Who can access the resource
  - Which resources can be accessed and what the user can do to the resource
  - How resources can be accessed
- No cost AWS account feature

### IAM

- **IAM user:** person or application that can authenticate with AWS account
- **IAM group:** collection of IAM users that are granted identical authorization
- **IAM policy:** document that defines which resources can be accessed and level of access with each resource
- **IAM role:** tool to grant a set of permissions for AWS service requests.

### Authenticating as an IAM user

- Programmatic Access 
  - Access Key ID
  - Secret Access Key
  - AWS CLI and SDK
- AWS Management Console
  - Authenticate using:
    - 12-digit account ID/Alias
    - IAM username
    - IAM password
    - Multi-factor authentication
      - Provides increased security
      - Requires unique auth code

### IAM: Authorization

- Permissions determine which resources and operations are allowed
  - Permissions denied by default
  - If explicitly denied, it is never allowed
- **Principle of Least Privilege**

### IAM policies

- Document that defines permissions
- Two types: identity and resource based
- Identity based:
  - Attach policy to IAM user, IAM group, IAM role
  - Specify:
    - Actions that may be performed by entity
    - What may not be performed
  - Single policy can be attached to multiple entities
  - Single entity can have multiple policies attached to it
- Resource-based policies
  - Attached to resource (ex: S3 bucket)

#### Resource-based policies

- **Resource based policies:** attached to a resource, not to a user or role
- Characteristics:
  - Specifies who has access to the resource and what actions they can perform on it
  - Policies are inline not managed
  - Only supported by some AWS services

### IAM groups

- Collection of IAM users
- Group is used to grant same permission to multiple groups
- User can belong to multiple groups
- No default group
- Groups cannot be nested

### IAM roles

- **IAM role:** IAM identity with specific permissions
- Similar to IAM user- attach permissions policies to it
- Not uniquely associated with one user, unlike IAM user- can be assumable by person, app or service
- Provides temporary security credentials
- Examples:
  - Used by IAM user in same AWS account as the role
  - Used by AWS service in same account as role
  - Used by IAM user in different account than role

## Securing a New AWS user account

### AWS account root user access vs IAM access

- Best practice: Do not use the root user account when necessary
  - Access to root user requires logging in with email and password used to create account
- Actions that can be only achieved by root user:
  - Update account root user password
  - Change AWS support plan
  - Restore IAM users permissons
  - Change account settings

### Securing a new AWS account: Account Root user

1. Stop using the account root user ASAP
   - Create IAM user and group, add user to the group
   - Remove account root user access keys
   - Enable password policy for users
   - Sign in with new IAM user credentials
   - Store account user credentials 

### Securing a new AWS account: MFA

2. Enable Multifactor Authentication
   - Require MFA for account root user and for all IAM users

- Options for retrieving MFA token
  - Virtual MFA compliant applications
  - U2F security key devices (YubiKey)
  - Hardware MFA options
    - Key fob/display card 

### Securing a new AWS account: AWS CloudTrail

3. Use CloudTrail
   - Track user activity on your account
     - Logs all API requests to resources in all supported services on account
   - Basic AWS CloudTrail event history enabled by default and is free
     - 90 days of account activity logged
     - Can create a trail and enable specified event alerting, creating a trail
     - Apply to all regions, create new S3 bucket for log storage
       - Configure access restrictions on buckets

### Securing a new account: Billing report

- Provide information about use of AWS resources and estimated cost for use
- AWS delivers report to specified AWS S3 bucket
  - Report is updated once per day
- AWS cost and usage report tracks AWS usage and provides estimate charges with AWS account

## Securing Accounts

### AWS Organizations

- Enables you to consolidate multiple AWS accounts so you can centrally manage them
- Security features:
  - Group AWS accounts into organizational units (OUs) attach different access policies to OU
  - Integration and support for IAM
    - Permissions to user are intersection of what is allowed by AWS 
    - Organizations and what is granted by IAM in that account
  - Use service control policies to establish control to establish control over AWS services and API actions that each AWS account can access

### AWS Organization: Service control policies

- **Service control policies (SCP):** offer centralized control over accounts
  - Limit permissions that are available to account that is part of an organization
- Ensures compliance with access control guidelines
- SCPs are similar to IAM permissions
  - They use syntax 
  - SCP never grants permissions
  - SCPs specify maximum permissions for an organization

### AWS Key Management Service (AWS KMS)

- Enables you to create and manage encryption keys
- Enables you to control use of encryption across AWS services and in applications
- Integrates with AWS CloudTrail to log all key usage
- Hardware security module (HSMs) that are validated by information processing standards (FIPS) 140-2 for protecting keys

### Amazon Cognito

- Adds user sign up, sign-in, and access from web and mobile apps
- Scales to millions of users
- Sign-in with social identity providers
- Helps to meet various security and compliance requirements

### AWS Shield

- Managed DDoS protection service
- Safeguards applications running on AWS
- Always-on detection and mitigation
- AWS Shield standard is enabled by default
- AWS shield advanced is an optional paid service
- Used to minimize application downtime/latency
- To contact the DDoS response team, need to have business or enterprise support

## Securing data on AWS

### Encryption of data at rest

- **Encryption:** encodes data with a secret key, makes it unreadable
  - Only those who have the secret key can decode data
  - AWS KMS can manage secret keys
- AWS supports encryption of data at rest
  - Data at rest = data stored physically
  - Can encrypt data stored on Amazons services
- Many regulations require encryption of data at rest

### Encryption of data in transit

- **Data in transit:** data moving across a network
  - Transport layer security
  - **AWS certificate manager:** provides a way to manage, deploy and renew TLS or SSL certificates
  - HTTPS provides a secure tunnel
  - AWS supports encryption in transit between services

### Securing Amazon S3 buckets and objects

- S3 buckets and objects are private and protected by default
- Essential to manage and control data access 
- Follow principles of least privilege
- Methods for controlling access to S3 data:
  - Amazon S3 block public access: simple to use
  - IAM policies: good option when user can authenticate using IAM
  - Bucket policies
  - Access control lists (ACL): Legacy access control mechanism
  - AWS Trusted Advisor: bucket permission check: free feature

## Working to ensure compliance

### AWS compliance programs

- Customers subject to many different security and compliance regulations and requirements
- AWS engages with certifying bodies and independent auditors to provide customers with info about policies, processes, controls established and operated by AWS
- Three broad categories:
  - Certifications and attestations
    - Assessment by a third-party auditor
    - Ex: ISO 27001, 27017,27018, ISO/IEC 9001
  - Laws, regulations and privacy
    - Provides security features and legal agreements to support compliance
    - Ex: EU GPDR, HIPPA
  - Alignment and frameworks
    - Industry or function- specific security or compliance requirements
    - Examples: Center for Internet Security, EU-US Privacy shield

### AWS config

- Assess, audit, evaluate configurations of AWS resources
- Use for continuous monitoring of configurations
- Automatically evaluate recorded vs desired configurations
- Reviewing configuration changes
- Viewing detailed config history
- Simplify compliance auditing and security analysis

### AWS artifact

- Resource for compliance-related information
- Providing access to security and compliance reports, online agreements
- Can be accessed from AWS Management console
  - Security, Identity & Compliance, Artifact
- Agreements on accounts
