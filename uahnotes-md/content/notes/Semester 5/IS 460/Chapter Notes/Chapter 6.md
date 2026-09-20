---
title: Chapter 6
---
## 6.1 - Protocol Types
### IP, TCP, UDP, TCP/IP
- **Protocol Number:** The value assigned to a protocol used by a network layer (L3) protocol
  - Common protocols:
    - **IPv6 protocol:** used for data communications over an IP network. IPv6 protocol is an addressing protocol used by routers to send a packet to the destination device
    - TCP is a connection oriented protocol used to ensure reliable transmission of data between network devices
    - UDP is a connectionless-oriented protocol used to transmit data between network devices
    - **Transmission Control Protocol (TCP/IP):** set of communication protocols used by internet or intranet devices. Creates a reliable connection between network devices. Manages the reassembly of packets into the original message into smaller packets for transmission. Each gateway device uses IP addressing to determine the route to correct destination device
    - **Neighbor Discovery Protocol:** internet protocol suite used in IPv6

### Protocol definition and key elements

- **Network protocol:** established set of rules enabling network device communication. Two categories
  - **Proprietary:** protocol that is developed a specific vendor for vendor product
    - Ex: Apple talk
  - **Standard protocol:** protocol that is developed by information tech organizations and adopted by the network industry (Ex: TCP/IP)
- Various organizations define standard protocols
- Three key elements: syntax, semantics, timing

### Network protocol functions

- **Data transfer:** synchronizes a network devices data rate and provides data sequencing
- **Encapsulation:** adds a header or trailer so data is transmittable
- **Packet segmentation:** divides packets into smaller segments at the the transport layer
- **Connection control:** ensures the transfer of connection oriented-data
- **Transmission control:** prioritizes Quality of Service and the security of packets
- **Addressing:** defines a devices address during network communications
- **Flow control:** operates at OSI Layer 4 and limits network congestion and data loss
- **Error control:** detects errors using the checksum bits

### Directory Services
- **Directory service (DS):** software system that organizes, manages, administers, locates network objects or resources
- Allows users to access network resources without being aware of a resource physical location
- Types of directory services:
	- Netware directory services (NDS) - Novell Netware uses NDS about network resources in a hierarchical tree structure
	- Active directory services (ADS): Used by Microsoft - Microsoft's version of NDS
### LDAP
- **Lightweight directory access protocol (LDAP):** accesses and maintains distributed directory information services over an IP network
- Commonly used to provide a central location for usernames and passwords
- Not secure transmission because data is stored in cleartext
- **LDAPS (LDAP over SSL):** Uses SSL/TLS to protect LDAP messages
- LDAP Uses TCP port 389 and LDAPS uses TCP port 636

## 6.2 - Distance vector protocol

### IGP and convergence

- **Autonomous system (AS):** a large network or collection of networks that has a unifying routing policy
- **Interior gateway protocol (IGP):** a type of routing protocol used for exchanging routing table information within an autonomous system. Three types of IGP protocols are distance vector protocol, link state protocol, advanced distance vector routing protocol
- **Convergence:** the state when all AS participating routers have the topological information. AS participating router attempts to exchange info about the network topology

### Distance vector protocol

- **Distance vector protocol:** routing protocol that uses distance vectors or hop count as the primary metric to determine the destination route of a packet
  - Sends full router table updates to neighboring routers every 10-90 seconds

| Characteristic    | Advantage                                                    |
| ----------------- | ------------------------------------------------------------ |
| Routing table     | Routinely sends routing table information to neighboring routers. |
| Best path         | Determines the best path using hop count. Hop count is the number of routers the data passes through to get to the destination device. |
| Route calculation | Uses the Bellman-Ford algorithm to calculate the best route. |

### RIP

- **Routing Information Protocol (RIP):** a distance vector protocol that employs hop count as the main routing metric
  - Network layer 3 protocol
  - RIP uses UDP port 520. RIPv1 was the original RIP version- replaced by RIPv2
- Characteristics of RIP:
  - Routers using RIPv1 send routing table to the neighboring routers every 30 sec
  - Max hop count is 15
  - RIPv1 updates neighboring router with broadcast messages. RIPv2 uses multicast messages
  - Full routing tables are sent as update instead of routing info
  - Metric used to determine best path is hop count or how many router the data passes through
  - RIP is not easily scalable
  - RIP convergence is slow

| Version | Classless or classful routing | IPv4/IPv6 support | Authentication support |
| ------- | ----------------------------- | ----------------- | ---------------------- |
| RIPv1   | Classful                      | IPv4              | No                     |
| RIPv2   | Classless                     | IPv4              | Yes                    |
| RIPng   | Classless                     | IPv6              | Yes                    |

### IGRP

- **Interior Gateway Routing Protocol (IGRP):** proprietary distance vector routing protocol used to send routing information within and autonomous system
  - IGRP updates the occurring network changes and uses error management
  - IGRP updates the network changes and uses error management
  - Network Layer 3 protocol
- Characteristics:
  - Routers send updates to neighboring routers every 90 seconds - only changes to the routing table
  - Maximum hop count is 255
  - Metric parameters:
    - Delay
    - Bandwidth
    - Reliability
    - Load
    - Maximum transmission unit (MTU) - largest protocol data unit (PDU) frame size in a layer 3 transaction
  - Proprietary (Cisco)
  - Poor scalability
  - Limitations on time to converge

|                         | RIP1            | RIP2            | IGRP            |
| ----------------------- | :-------------- | :-------------- | :-------------- |
| Protocol type           | Distance vector | Distance vector | Distance vector |
| Metric                  | Hop count       | Hop count       | Bandwidth/delay |
| Administrative distance | 120             | 120             | 100             |
| Hop limit               | 15              | 15              | 255             |
| Convergence speed       | Slow            | Slow            | Slow            |
| Table update intervals  | 30 Seconds      | 30 Seconds      | 90 Seconds      |
| Classless               | No              | Yes             | No              |
| VLSM support            | No              | Yes             | No              |
| Protocol and port       | UDP port 520    | UDP port 520    | IP protocol 9   |

## 6.3- Link state, BGP and EIGRP protocols

### Link state protocol

- **Link state protocol (shortest path first protocol):** IGP routing protocol used in packet switching networks. Has a full network topology picture by using three tables per enabled router
  - Topology and neighbor connectivity information allows each router to calculate the best path to each network destination
  - Designed for efficient bandwidth usage

| Characteristic       | Advantage                                                    |
| -------------------- | ------------------------------------------------------------ |
| Router communication | Floods information to each AS router about the state of routers directly connected links. |
| Router database      | Uses link state information to build a link-state database, providing a full network topology picture. |
| Speed                | Uses bandwidth efficiently.                                  |
| Resource utilization | Intensive use of CPU and memory                              |

### OSPF

- **Open Short path first (OPSF):** an IP routing protocol used to send IP routing information over a single AS
  - OSPF is a layer 3 protocol using IP protocol 89
  - Does not need TCP or UDP support and is often encapsulated in an IP datagram
- Lowest-cost path main metric is based on bandwidth. Data path is determined by choosing the lowest cost path to the final destination network
- Characteristics
  - Uses a link state advertisement (LSA) message to distribute changes or initial startup information for other routers
  - Table contains full knowledge of topology
  - Each network enabled router in the AS builds a database describes the AS topology
  - Routers traffic within a single AS
  - Router database is used to calculate the routers routing table using a Shortest Path First (SPF) algorithm
  - Provides support for multiple paths of equal cost
  - Authenticates protocol exchanges
  - Supports IPv4 and IPv6

### BGP

- **Border Gateway Protocol (BGP):** an exterior gateway protocol enabling the internet to exchange routing information between autonomous systems
  - Internet has thousands of smaller autonomous systems connected together
  - Routing protocol for routing the data path through multiple autonomous autonomous systems
  - Uses TCP port 179
- Steps in the BGP routing algorithms
  - BGP assigns first valid path as the current best path
  - BGP compares best path with the next path in the list:
    - If next best path is preferred, BGP replaces the best path with this path
    - If the best path is preferred, BGP leaves the current path as the best path
  - BGP continues to the next path in the list until reaching the end of valid paths
- Metrics used in BGP best path decision:
  - Weight - Cisco proprietary local router between 0 and 65,535
  - Originate - prefers the path local router originated
  - AS_Path - prefers shortest AS path
  - Origin code- Prefers lowest origin code. IGP is lower than EGP, EGP lower than incomplete. Incomplete is the highest

### Hybrid

- **Enhanced Interior Gateway Routing Protocol (EIGRP):** distance vector routing protocol used to send routing protocol in AS
  - Uses IP Protocol 88 (built in transport layer support)
  - Developed to address limitations of IGRP but also to add link state protocol, EIGRP is a hybrid protocol
  - Major difference between IGRP and EIGRP is that EIGRP uses topology table. Stores information advertised by neighboring routers about known routes and details about distance, path reliability, reported distance, total delay.
  - Has a maximum hop count of 224

| Characteristic    | Protocol information                                         |
| ----------------- | ------------------------------------------------------------ |
| Convergence speed | EIGRP is faster than IGRP                                    |
| Efficiency        | EIGRP exchanges router information more efficiently.         |
| Scalability       | EIGRP addresses the IGRP scalability problem.                |
| Compatibility     | EIGRP is backward compatible with IGRP.                      |
| Communication     | EIGRP uses a Hello packet to notify neighboring routers the router is operative. If no Hello packet is sent after a certain time, the router is considered offline. |
| Routing table     | EIGRP updates neighboring routers with changes only, not an entire routing table. |
| Quality           | EIGRP improves voice and video quality.                      |

## 6.4 - Common Protocols

### Management, communication, and security protocols

Three common protocols:

- **Management protocol:** defines the policies to monitor, manage, and maintain the network
- **Communication protocol:** defines the data communications format and rules
- **Security protocol:** defines how to secure data transmissions

### NMP and SMB

- **Server Message Block:** a client-server communication protocol, used for sharing access to files, printers and serial ports. SMB can carry transaction protocols for interprocess communications and is implemented in Windows
- **Network management protocol (NMP):** a suite of protocols defining processes, procedures and policies for network management
  - Monitor a network 24/7 in real time and provide network stats to a network admin
  - Common protocols are Internet Control Message Protocol (ICMP) and Simple network management protocol (SNMP)
- Information an NMP protocol provides:
  - Status of a host
  - Host availability
  - Network latency
  - Packet loss
  - Network errors

### ICMP

- **Internet Control Message Protocol (ICMP):** protocol used by network devices to communicate problems with data transmission. ICMP is a layer 3 protocol. No port number is used since this is not the network transport protocol. TCP and UDP are network layer protocols so all protocols operating below the transport layer don't use port numbers. 
- ICMP is a component of the TCP/IP protocol stack. Accompanies IP to provide a process for sending control and error messages
- ICMP function is to report any IP operation errors. Some common ICMP error messages:
  - Time to Live (TTL)- occurs when datagram TTL has reached zero but the datagram has not reached the final destination
  - Destination unreachable - Occurs when the IP packets destination host, network, port number unreachable
  - Parameter problem - Occurs when a device finds a problem that is not covered in any ICMP message type
  - Packet too big - Occurs when a datagram is too large for the network

### SNMP

- **Simple Network Management Protocol (SNMP):** network protocol for monitoring and managing network devices in an IP network. SNMP is an application layer protocol (Layer 7). Uses TCP ports 161 and 162
- **Managed device (network element):** network node that implements an SNMP interface that allows access to the network node's information. Managed device can be any type of device. SNMP manager is a system that monitors that monitors and controls network elements activities using SNMP. SNMP agent is the software that urns on a network element and collects and maintains info on network element. SNMP manager may request information from network element or set a configuration parameter on a network element. 
- **SNMP trap:** an alert message sent from an SNMP manager to notify the SNMP manager of an event at a network element
  - Management Information Base (MIB): An ASCII text file that describes SNMP elements as a list of data objects

### ARP

- **Address Resolution Protocol (ARP):** network protocol for mapping dynamic IP addresses to physical device (MAC address)
  - Works between the data link and network layer protocol (L2 and L3)
  - Does not use a specific TCP port
- **Dynamic ARP inspection (DAI):** used to detect and reject invalid and malicious ARP packets
- ARP table is used to lookup the MAC address corresponding to the IP address
  - If not in the table, source device broadcasts an ARP request
    - Broadcasts message asking which device has requested IP address
    - IP device sends unicast message back containing requested IP devices MAC address

## 6.5 - Secure Protocols

### SSL/TLS

- **Secure Sockets Layer (SSL)/ Transport Layer Security (TLS):** cryptography protocols used to provide secure communications between devices over a network
  - Transport Layer Security is more secure. TLS replaced SSL in 1999. SSL term is still widely instead of TLS
- **Security certificate (SSL certificate):** issued by a certificate authority and provides a security level that authenticates a website to the certificate providing a secure connection. 
  - Operates at OSI L6
- TLS implemented on top of TCP to encrypt application data layer protocols
  - Uses encryption algorithms to scramble the transmitted data
  - Destination device decrypts the transmitted data for presentation of application
- Applications that use SSL/TLS:
  - Email
  - Instant Messaging
  - Voice over IP (VoIP)
  - Hypertext Transfer Protocol Secure (HTTPS)

### Symmetric cryptography

- Symmetric encryption is used by TLS
- **Symmetric encryption:** an encryption algorithm that uses the same key to encrypt and decrypt the data
- **Symmetric key or secret key:** key used in symmetric encryption 
- Two classes of symmetric encryption: 
  - **Stream cipher:** a symmetric encryption algorithm that encrypts data one bit at a time
  - **Block cipher:** a symmetric encryption algorithm that encrypts data one block at a time
- Symmetric encryption is faster and more efficient than asymmetric encryption because symmetric encryption uses shorter keys and simpler operations
  - Used in many cryptographic protocols such as HTTPS and IPSec

### Asymmetric cryptography 

- TLS also uses asymmetric encryption.
- **Asymmetric encryption (public key encryption):** two different but mathematically related keys used to encrypt and decrypt a message
- **Public key:** not secret and openly avaliable
- **Private key:** secret and is only available to the key-pair owner
- Enables two entities to securely exchange a message
- **Public Key Infrastructure (PKI):** a framework for managing digital certificates and public keys

### SSH

- **Secure shell (SSH):** cryptographic network protocol for securely operating a network service over an unsecured network
  - SSH client connects to SSH server using a client-server model
  - Designed as a replacement for Telenet
  - Uses TCP port 22 by default
- Provides security by using message authentication codes (MAC)
- Any network service supports protocol tunneling, any network service can be secured by SSH
- **Protocol tunneling:** the encapsulation of a protocols packets with the packets of a another protocol
- SSH is used in SSH file transfer and secure copy protocol (SFTP and SCP)
- SSH can be used for public authentication to provision access without requiring a user password for each login
- SSH authentication allows SSO. 
- Public key is stored on SSH server and the users private key to authenticate the user

### IPSec

- **Internet Protocol Security (IPSec):** protocol suite for securing data communications over an IP network 
  - Ensures authenticity, integrity, confidentiality, anti-replay of an IP packet. 
  - Network-layer protocol (L3)
- Two main protocols:
  - **Authentication Header (AH):** an IPSec protocol providing three features of IPSec (authentication, integrity, anti-replay) for IP packet
    - Ensures data integrity by using a message digest and data authenticity by using a shared secret key to create a message digest
    - Protects against replay attack by using the sequence number in AH header
    - AH authenticates an entire IP packet
  - **Encapsulating Security Protocol (ESP):** IPSec protocol providing all 4 features of IPSec (authenticity, integrity, confidentiality, anti-replay) for an IP packet. ESP provides confidentiality by encryption, using shared key between a data sender and a data receiver. Uses same AH algorithm for integrity and authentication. ESP only authenticates IP payload

### IKE and MIB

- **Internet key exchange (IKB):** secured management protocol used for communications between two network devices
  - Normally uses the UDP protocol
  - IPSEC uses IKE to negotiate and authenticate IPSec SAs
- **Management information base (MIB):** database containing SNMP device configuration information. Uses MIB to monitor network devices. Can be used to monitor IPSEC when IPSec is using IKE



## 6.6- Mail, web and remote access protocols

### Mail protocol

- **Simple Mail Transfer Protocol (SMTP):** network protocol for sending, receiving and relaying outgoing emails
  - L7 
  - Uses TCP port 25 and SMTPS port 587
  - SMTP used to send email from server to server
- Post Office Protocol (POP) and Instant Message Access Protocol (IMAP)
- HTTP is not exclusively a mail protocol but is used in web-based email systems - Hotmail, Yahoo, Gmail
- HTTP uses TCP port 80

| Feature                 | POP                          | IMAP                         |
| ----------------------- | ---------------------------- | ---------------------------- |
| Typical usage           | Access from single device    | Access from multiple devices |
| Email retrieval         | Entire email or headers only | Any email subpart            |
| Port                    | TCP 110 (POPS uses TCP 995)  | TCP 143 (IMAPS uses TCP 993) |
| Email folders on server | No                           | Yes                          |
| Email search on server  | No                           | Yes                          |

### HTTP

- **Hyper text transfer protocol (HTTP):** a network protocol for distributing graphics, audio, video,text and hyperlinks on networks
  - An application layer protocol 
  - L7
  - TCP Port 80
- Mostly used for communication between a browser and the WWW (World Wide Web)
- Web browser submits HTTP request message to a server returns response message
- Server provides content to the web browser (ex: HTML)

### HTTPS

- **Hypertext transfer protocol secure (HTTPS):** HTTP over SSL or HTTP over TLS is an extension of the hypertext transfer protocol that uses SSL/TLS to establish an authenticated and encryption between a client and a server
  - Used for secure data exchange between a web browser and a web server
  - An application layer protocol (L7)
  - TCP 443
- HTTPs relies on cryptographic services provided by SSL/TLS protocol to secure HTTP data
  - SSL/TLS uses digital certificates for authentication, encryption for data confidentiality, message authentication codes (MAC) for data integrity
  - HTTPS supports mutual authentication. HTTPS protects against man-in the middle attack
  - Eavesdropping and tampering of data exchanged between web browser and web server

### FTP

- **File Transfer Protocol (FTP):** a network protocol for transferring files between two network device. FTP is an application layer protocol (L7)
  - FTP uses TCP ports 20 and 21
  - FTP is a client/server protocol, using a command and data for communication
  - FTP transfers between two devices
- **Trivial file transfer protocol (TFTP):** a simpler FTP version primarily used for transferring network device configurations using port 69. Preboot Execution Environment (PXE) uses TFTP to downloading network software

| Characteristic | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| Backup         | Used to backup data at regular intervals from one device to another device. |
| Replication    | Duplicates data from one device to another device in real time to provide higher availability and resilience. |
| Data loading   | Using the cloud to transfer load data to a remote device.    |

### FTPS and SFTP

- **FTPS:** known as FTP over SSL 
  - Extension of file transfer protocol that uses SSL/TLS to provide communication security
  - FTPS supports all SSL/TLS cryptographic protocols that use client and server certificates for authentication
- **SSH file transfer protocol (SFTP):** known as SSH-FTP or Secure FTP- extension of SSH protocol that enables secure file transfer capabilities between network hosts. Provides remote file system management functionality that enables an application list of the contents of remote directory. 

| Protocol | Security mechanism | Port                                             |
| -------- | ------------------ | ------------------------------------------------ |
| FTP      | None               | TCP 20 (data channel) TCP 21 (control channel)   |
| FTPS     | FTP over SSL/TLS   | TCP 989 (data channel) TCP 990 (control channel) |
| SFTP     | SSH                | TCP 22                                           |

- Used to securely transfer files between networked hosts
- FTPS uses SSL/TLS to create authenticated and secure communication link between two hosts
- FTPS and SFTP not compatible with each other
  - SFTP client cannot connect to an FTPS server and FTPS client cannot connect to an SFTP
- 