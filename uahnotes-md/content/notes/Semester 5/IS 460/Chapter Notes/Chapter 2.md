---
title: Chapter 2
---

 ## Chapter 2.1
- ### Conceptual model strucuture
- **Conceptual Model:** Representation of a system or process. Used in networking to help understand end-to-end network communication
	- **Open systems interconnection (OSI) model:** seven-layer network conceptual model created by international organizations for standardization
	- **Department of Defense (DoD) model:** four layer network conceptual model implemented as internet protocol suite
- Both OSI and DoD models use abstraction layers to describe end-to-end net communication
	- **Abstraction layer:** generalization of system, process or device
		- Can describe network protocols
			- Ex: IP
	- **Network protocol:** A set of rules specifying how data is formatted, processed and transmitted between the devices on a network
	- OSI = 7 layers  - Hardware dependent
	- DoD = 4 Layers - Protocol Dependent
	- ![](../assets/0abe4ca5a4b86f0aa5195555a5f95cdf.png)![](../assets/5da50825e2299e559ab3e170d5de89f6.png)
	- DoD model is read horizontally even though it is presented vertically
### Encapsulation and decapsulation
- Abstraction layers of both the OSI and DoD models add the information data needs to traverse a link
- **Encapsulation:** process of adding a header or trailer so data is transmittable
- **Header:** an information field added before a piece of data before transmission
- **Trailer:** information added to end of data before transmission
- **Protocol data unit (PDU):** Data encapsulated with an abstraction layers header or trailer
- **Payload:** Actual data being transmitted and excludes the headers or trailers added by each abstraction layer
- **Decapsulation:** process of removing a header or trailer so data is receivable

## Chapter 2.2
![](../assets/68d70ba42b0396d0a71c5acfca9e64ad.png)
![](../assets/702017161b8b2a6f848f1c0f6ed7aaf6.png)
### Layers 5,6,7
- Top down approach because encapsulation and decapsulation
- **Layer 7** - OSI model application layer- network protocol interacts with a network aware application
- **Layer 6** - OSI model presentation layer, data prepared for transmission between application layer and session layer
- **Layer 5** OSI model session layer, where a data transmission channel known as a session is established between communicating devices
### Layer 4
- OSI model transport layer
- **TCP:** a network protocol used to establish a guaranteed, connection oriented communication channel between communication devices 
- **User Datagram protocol (UDP):** a network protocol used to provide non-guaranteed, connectionless data transport for communicating devices
- **Segment:** PDU created by TCP, includes TCP header consisting of connection state info
- **Datagram:** PDU created by UDP, includes UDP

### Layer 3
- Receives logical address information needed to reach recipients network
- Divides into smaller chunks of data for transmation
- **Internet Protocol (IP)** network protocol used to address data sent over internet or another network 
- **Packet:** PDU created by IP, includes IP header consisting of logical adress
- Packets should take most efficient route
- **Router:** a layer 3 networking connecting at least 2 networks
- **Routing protocol:** a network protocol used by a router to determine the most efficient route 

### Layer 2
- OSI model data link layer
- **Frame** is the PDU created by layer 2 containing data transmission parameters and physical address
- **Logical link control** a layer 2 sublayer data flow control, error detection and error correction
- **Media access control** a layer 2 sublayer providing physical address and frame synchronization
- One central node connecting several nodes together
- **Switch:** layer 2 networking device serving as a central node for at least 2 other nodes

### Layer 1
- OSI model physical layer where a payload is transmitted across a network medium
- Wireless signal transmits a payload using a series of radio waves
- **Radio wave:** artificially generated energy that radiates electrical current into open space
- PDU not created at layer 1
- Binary number is a number expressed in a base-2 numeral system
- A **binary number** is a number express in a base-2 numeral system also called the binary numeral system

## Chapter 2.3
