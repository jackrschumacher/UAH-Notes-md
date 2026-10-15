---
title: Chapter 11
---
## 11.1 - Data center

### Data center types

- **Data center:** dedicated space within building, multiple buildings, collection of buildings that house computing resources and related equipment
- Data center types:
  - **Enterprise data center:** On-premises data center used to process internal data and host mission-critical applications for a single organization. In house team oversees data center
  - **Colocation data center (carrier hotel):** off-premises, leasable data center where organization deploys computing resources and associated equipment. Designed to meet a data centers power, cooling, communications, etc. requirements. Single organization can lease an entire colocation data center
  - **Managed data center:** data center where an organization uses a third party to oversee leased facility, compute resources, associated equipment
  - **Cloud data center:** off-premises, internet-accessible data center that cloud service provider uses to offer subscription services. Uses cloud data center to subscribe to service instead of deploying resources a service requires
  - **Edge data center:** Smaller data center located as close as possible to end user- designed to minimize latency and lag. Organization can deploy multiple to meet needs/ satisfy bandwidth requirements

### Three tiered architecture

- Suggests to change design from flat network to hierarchical network
  - Hierarchical network is easier to manage and troubleshoot
- **Data Center Interconnect (DCI):** links data center locations to share resources. 
  - Hierarchical model contains core, distribution and access
- **Core layer:** backbone of network, provides high-speed connection between different distribution layer devices
- **Distribution layer:** connects the access layer to core layer, determining access and policy-based connectivity
- **Access layer:** allows end users to access network and connect end-user devices 

### Data center infrastructure

- Designed to handle large amounts of traffic with minimal latency
- Bandwidth and transmission requirements are commonly satisfied through use of DCI technology 
- **Data center interconnect (DCI):** includes next-gen optics cabling and supporting infrastructure connecting two or more geographically separate data centers  
- Data center computing resources:
  - Servers
  - Network infrastructure
  - Storage infrastructure
- **East-West traffic:** refers to traffic flow between devices in data center
- **North-South Traffic:** traffic flowing into and out of the data center. Southbound traffic enters the data center, northbound traffic exits the data center

| Physical computing elements (IT hardware) | IT infrastructure support |
| ----------------------------------------- | ------------------------- |
| Servers                                   | Redundant power sources   |
| Switches                                  | Temperature control       |
| Routers                                   | Humidity control          |
| Data storage devices (Ex: SAN)            | Building security         |
| Cabling                                   | Fire suppression          |

### Data center management

- **Data center infrastructure management (DCIM):** combines IT and data center facility management disciplines to optimize data center performance
  - Uses discover, monitoring, reporting and visualization to control physical data center performance 
  - Provided by managed service provider, third party or DCIM software

| DCIM component              | Description                                         |
| --------------------------- | --------------------------------------------------- |
| Inventory information       | Servers and network equipment                       |
| DCIM asset visualization    | Dashboard and reports                               |
| Physical connectivity       | Rules used to validate connectivity                 |
| Systematic workflow         | Supports workflow items (Ex: planning, and auditing |
| Enterprise class monitoring | All data center nodes monitored                     |

## 11.2 - Virtual

### Virtualization

- **Virtualization:** use of software to create simulated version of physical computing resource. Foundation of cloud computing. Allows for efficient use of physical computer hardware through creation of virtual machines.
  - **Network Virtualization (NV):** method to deliver physical network resources from hardware to software
  - **Virtual machine (VM):** virtualization of a computer system
- **Hypervisor (Virtual machine monitor- VMM):** software or firmware used to virtualize hosts machines hardware platform 
- **Host machine:** machine used by a hypervisor to virtualize host machines hardware platform
- **Guest machine:** VM running on host machine
- **Logical isolation:** virtualization feature enabling guest machine to act like an independent machine

- Virtual terms:
  - **Virtual network computing (VNC):** cross-platform screen sharing platform used to remotely control another computer
  - **Remote access:** remote control of computer by using a device connected by a network. Allows access to desktops and files
  - **Network functions virtualization (NFV):** replacement of network appliance hardware with virtual machines that use hypervisor 
  - **Virtual switch (vSwitch):** software program that enables VMs to communicate with other VMs. Directs network communication checking data packets before moving to destination. 
  - **Virtual network interface card (vINC):** configuration of a VM connected to a network. VM can be configured to have multiple vNICs
  - **Virtual IP (VIP or VIPA) adress:** IP address that is shared by both members of high availability server pool on same subnet and does not correspond to physical network interface

### Hypervisor types

- **Type 1 hypervisor:** native/bare metal- runs directly on host machine
- **Type 2 hypervisor:** hosted hypervisor, runs an application on existing operating systems

| Consideration | Type 1                            | Type 2                                          |
| ------------- | --------------------------------- | ----------------------------------------------- |
| Use           | A system built for virtualization | Adding virtualization to a traditional computer |
| Deployment    | Server                            | Workstation                                     |
| Performance   | Better logical isolation for VMs  | Adequate logical isolation for VMs              |
| Cost          | More expensive than type 2        | Less expensive than type 1                      |

### Virtualization exploit

- **VM escape:** virtualization exploit where a process escapes a guest machines logical isolation to interact with the host
- **VM sprawl (virtualization sprawl):** virtualization exploit where attacker creates VM amount that consumers resources
- **VM lifecycle management:** series of procedures where VM is created, maintained, monitored and decommissioned

## 11.3 - Cloud 

### Cloud computing

- **Cloud computing:** computing model where IT resources are offered on demand over internet
- **Cloud service provider:** offers cloud computing
- **Infrastructure as a Service (IaaS):** cloud computing model that offers infrastructure components on demand. Infrastructure components include network, storage, servers, virtualization
- **Platform as a Service (PaaS):** cloud computing model that offers hardware and software tools for application development and deployment. Includes networking, storage, server, virtualization
- **Software as a Service (SaaS):** cloud computing model that offers software application over the internet. SaaS provider manages access to applications and data
- **Anything as a Service (XaaS):** refers to products, tools, technology that are offered to service over the internet

### Cloud Deployment models

- **Public cloud:** cloud deployment that is provisioned for use for general public. Public cloud exists on cloud providers premises
- **Private cloud:** cloud deployment model that is provisioned for exclusive use by single organization. May be managed and operated by organizations that own that own the private cloud. 
  - **Virtual Private Cloud:** Private cloud where cloud infrastructure resides within public cloud
- **Hybrid cloud:** cloud deployment model where public and private clouds are bound together by proprietary technology. Enables sharing of data between cloud deployments
- **Community Cloud:** Cloud deployment model that is provisioned for exclusive use by organizations within common computing concerns. Concerns: may be owned, managed, and operated by organizations in community, or by managed service provider (MSP). May exist on or off premises.

### IaC

- Cloud network can be configured via a programmatic approach
- **Infrastructure as code (IaC):** method of managing and provisioning computer data centers through machine-readable files instead of hardware configuration tools
  - May use either scripts or declarative definitions to desired state
- **Desired State:** IaC feature that declares infrastructure final or desired state instead of configuration by step-by-step approach. Includes both physical equipment and associated configuration resources
- Typically used with continuous delivery- teams work together under set of rules to deliver applications and supporting infrastructure (declarative IaC or procedural IaC)
- **Declarative IaC:** set of parameters instructing software on how system needs to be configured once process is finished
- **Procedural IaC:** set of operations on how system reaches correct configuration. Includes physical equipment and associated configuration resources
- **Overlay network:** virtual network abstraction layer built on top of existing physical network infrastructure. Centralize networks management and control planes and SDWAN - software-defined network centralizing multilocation management

### Cloud connectivity

- **Point of Presence (PoP):** artificial demarcation point connecting communication entities. Normally located in a data center, houses, servers, and switches. Proximity of PoPs and internet exchange points is factor in how traffic is able to traverse internet
- **Private Service Connect:** allows private direct circuit across VPC networks belonging to different organizations - used to access Google APIs
- **Leased line:** telecommunications service delivering high-speed internet access using customer-specific leased connection
- **Virtual Private Network (VPN):** enables private connection between 2 or more devices on public network

## 11.4- Virtualization and networking

### Software-defined networking

- Overlay network is example of IaC
- **Overlay network:** virtual network abstraction layer built on top of existing physical network infastructure
  - Many modern networks leverage at least one overlay network technology to improve performance without additional investment in network equipment
  - Creates software defined network or software-defined WAN
- **Software-defined networking:** an overlay network technology that centralizes networks management and control planes
- **Software-defined wide area network (SD-WAN):** software-defined network centralizing multi-location networks management and control planes
- SDN can use northbound and southbound APIs to direct traffic

- **Secure access service edge (SASE):** convergence of WANs or SD-Wans and network security into single cloud service model. Supports multiple cloud services

### Software-defined visibility and APIs

- Can be used to monitor network traffic on the cloud or on premises network
- **Software-defined visibility (SDV):** technologies enabling network traffic visibility to any monitoring device regardless of location on network. Can use APIs to integrate with other services but to be aware of vulnerabilities. 

## 11.5 - Network storage

### Storage

- Can include both HDD and SSD and external storage like USB flash drive. Local storage supplies both higher storage throughput and lower latency. Local storage limits capacity, increases the risk of data loss
- **Network storage:** collection of network-accessible and manage storage resources which allows multi-user access, increases scalability, provides redundancy
- Network storage implementations:
  - **Network-Attached storage (NAS):** file storage connected to network, allows multiple users and devices to share data through centralized location. NAS mostly used in a home or small office
  - **Storage area network (SAN):** high-speed network providing access to network storage device. Mostly used in business or enterprise applications

| Feature             | Local storage             | Network storage               |
| ------------------- | ------------------------- | ----------------------------- |
| Accessibility       | Direct                    | Network                       |
| Speed               | Usually higher            | Dependent on network speed    |
| Capacity            | Limited to physical drive | High with scalability         |
| Sharing             | Difficult                 | Easy                          |
| Backup and recovery | Manual/Local              | Automated/centralized         |
| Costs               | Usually lower             | Higher initial and management |

### SAN

- Most practical to use in business or enterprise environment
- SAN has interconnected hosts, switches, storage devices and higher network speed access, salability, data management, virtualization support compared to NAS
- NAS is more cost effective and easier to setup but does not offer performance and reliability of SAN
- SAN types:
  - **Fibre Channel (FC):** high-speed data transfer technology tat connects computers, servers and storage devices
  - **Fibre Channel over Ethernet (FCoE):** storage networking technology allowing FC traffic to transmit over Ethernet networks
  - **Internet Small Computing System Interface (iSCSI):** used to link data storage device over network and facilitate data transfers
  - **InfiniBand:** high-speed networking technology primarily used for interconnecting servers and storage devices in high-performance computing environments, enterprise applications

| SAN        | Thoughput     | Latency                         | Cost                  | Reason to use                                                |
| ---------- | ------------- | ------------------------------- | --------------------- | ------------------------------------------------------------ |
| FC         | Highest       | Lowest                          | High                  | High performance, mission critical applications              |
| FCoE       | Lower than FC | Based on Ethernet network speed | Usually lower than FC | Outside data center application or infrastructure cost savings |
| ISCSI      | Lowest        | Highest                         | Lowest                | Cost effective and easy to deploy                            |
| InfiniBand | High          | Low                             | Highest               | High performance, mission critical applications              |

### iSCSI SAN

- Storage networking technology that allows clients to connect to remote storage devices over TCP/IP network
- Encapsulates SCSI commands with IP packets, transport block-level storage data over standard network 
- Operates differently from file access protocols
- Usage recommendations:
  - Use separate LAN segments for better isolation 
  - Hardware-accelerated network cards for better data exchange performance
  - Configure iSCSI-related hardware and network settings

### iSNS

- **Internet Storage Name Service:** primarily used in SANs, technology that facilitates discovery, management, and configuration of TCP/IP storage network iSCSI
  - Simplifies management of networks and enhances reliability and scalability
  - Stores properly authenticated information submitted by registration request in iSNS database
  - Local iSNS server can be configured and enabled for use by initiator and storage system
  - Storage system will automatically register IP, node name, portal groups with iSNS server when iSNS service started 
- Components of iSNS:
  -  **iSNS protocol (iSNSP):** based on client-server model using TCP/IP transport, enabling communication between iSNS and iSNS server. iSNSP specifies how iSNS clients and servers 
  - **iSNS clients:** devices (initiators and domains) that register themselves with iSNS server and is registered in common discovery domain
  - **iSNS servers:** provide registry to store information about iSCSI and other SCSI devices on network, including capabilities and state. Enables devices to discover each other and learn about resources available in storage network
  - **iSNS database:** repository maintained by iSNS server that holds registered information of all devices in storage network. Database is essential for efficient discovery and management of storage devices, keep track of data status and capabilities