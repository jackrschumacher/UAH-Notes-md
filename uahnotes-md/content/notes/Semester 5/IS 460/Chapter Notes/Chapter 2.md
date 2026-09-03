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

## Chapter 2.2 - OSI Model Layers
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

## Chapter 2.3 - DoD model layers

![](../assets/b508cb8c43a51a7f84143a7f3d7788d0.png)
### Application Layer
- Comparable to OSI model layers 5,6,7
- Application layer is the DoD models highest layer where a network-aware application interacting with transmitted data
- Application Layer Prepares data for transmission to the transmission layer
- Examples of application layer functions:
	- Remote access between nodes for troubleshooting
	- Email services between email client and server
	- File transfers between file transfer client and file transfer server
	- 
### Transport Layer - Layer 4
- DoD model layer where end-to-end payload delivery from source to destination
- Port number is a 16-bit unsigned number that uniquely identifies a network application or service on a host 
	- Associate a payload with a specific process or service
- TCP header is a 10-field,20-byte header containing connection and payload delivery details for a segment
	- Used to establish a three-way handshake for payload delivery
- ![](../assets/906d2ef1821118d677635138d4e55a4b.png)
- UDP Header, 4-field, 8-byte header containing connection and payload delivery details for a datagram
	- Used for best-effort payload delivery (non-guaranteed)
- ![](../assets/b77bddfaba84ac1f84869cb975896589.png)
### Internet Layer - Layer 3
- DoD model layer where hop-to-hop data delivery from source to destination occurs
- **IP header** is a header containing connection and payload data delivery details for a packet
	- IPv4
		- 14 field,d 20 to 60 byte header container connection and payload delivery details for the packet
		- 32-bit address 
		- ![](../assets/616411af82689fa707baf211dce9963e.png)
	- IPv6
		- 8-field, 40 byte header that contains connection and payload delivery details for an IPv6 packet
		- Unique 128-bit number assigned to a network interface controller
		- Can not be transmitted over IPv4 network without additional encapsulation
		- ![](../assets/72bfc4eed791dbb77a8a0877dd62c21f.png)
- ### Network access layer
	- OSI models layers 1 and 2
	- **Network access layer** - DoD model layer where data transfer between two devices on the same network occurs
	- **Institute of Electrical and Electronics Engineers-** a professional organization that advances 
		- IEEE 802 LAN/MAN standards committee sets standards for LAN tech
	- **Ethernet frame** is a 6 field, 64 byte header
	- **Media access control (MAC) address** a unique 48-bit identifier burned into a network interface controller
	- **Network Interface controller (NIC)** or **Network interface card (NIC)** is hardware connecting a networked device to bounded media
	- ![](../assets/5b5937303bf4dd3a718beaa0f98c5f98.png)
## 2.4 - Networking Devices

![](../assets/7a94aae4a8f58a03c9aa28122b02fd42.png)
### Layer 1 devices
- **Networking Device:** used to establish network connectivity
- **Networked device:** connected to the network
- **Hub:** legacy device used as a central node to provide connectivity to multiple devices
- **Repeater:** a networking device used as an adapter to connect different network medium
- **Media converter** a networking a device used as an adapter to connect different network mediums
	- Ex: Convert coax to twisted pair
- **Modulator/demodulator (==modem==)** a networking device used to convert a digital data signal to or from an analog carrier signal

### Layer 2 Devices
- **Bridge:** legacy networking device used as a central node connecting 2 network segments
	- Uses destination MAC address in frame to determine transmit location
	- Legacy because of of only 2 ports
	- Precedes switches
- **Switch:** Central node for at least 2 other notes
	- Provides more ports than a bridge
	- Uses a MAC address table  -Physical address and port of a device
- **Wireless Access point (WAP)** Central node for at least 2 wireless nodes
	- Can operate as a standalone or a bridge between LAN and VLAN
	- Provide both bridging and switching capability to wireless clients

### Layer 3 devices
- Layer 3 devices serve as a node used to connect and internal network to an external network
- Can refer to a layer 3 device as a boundary, gateway or edge device
- **Router:** a layer 3 networking device connecting at least 2 networks
	- Large network is typically divided into multiple subnets, to improve network performance
	- Switch is unable to communicate across subnets without a router
- **Routing table:** a rule table determining how a router routes a payload based on the destinations IP
- **Layer 3 switch:** layer 3 capable switch, a switch providing both layer 2 and layer 3 functions
	- Considered a multifunction device
- **Multifunction device (MFD):** a single device capable of providing multiple functions
- Most WLANs require multiple WAPs to provide sufficient coverage
	- Centrally managed switch is considered a multifunction device
- **Wireless LAN Controller (WLC):** a centralized device used to control and configure multiple managed WAPs

### Layer 4 devices
- Make forwarding decisions during payload transport
- Many layer 4 devices function both at layer 4 and the upper level layers for payload transport
	- Intrusion detection system (IDS)
	- Intrusion prevention systems (IPS)
	- Firewalls
- **Load balancing:** the act of distributing network traffic among multiple devices to improve performance and prevent overload
- **Load balancer:** either a hardware device or software service used to enforce load-balancing configurations
- **Voice over IP (VoIP):** a protocol group used to enable analog telephone conversations, or telephony, to occur over the internet
	- **Voice gateway:** a hardware device or software service used to convert telephony into digital packets for transmission via VoIP
- **Intrusion detection system (IDS):** a device or a software application that detects a malicious activity/ security policy violation
- **Intrusion Prevention system (IPS):** IDS that blocks threat to the network
- **Firewall:** a network device or a software program that controls inbound and outbound traffic based on a set of rules
- **Proxy server:** a network device or a software program intended to protect internal nodes by acting as an intermediary device for external network resources

## 2.5 Networked devices

### Client networked devices
- **Networked device:** a device connected to a network
	- Intended for one user or service
	- Networking device is intended for multiple users or multiple services
	- Could be a client, server or peer
	- Client accesses a network resource from as a client, server or peer
	- Client accesses a network resource from a server, but does not share network resources with other clients
	- A server shares a network resource with a client
	- Peer shares and accesses a network resource
- ![](../assets/55ff65c2794394fc48d43b1a3ff6eb2d.png)
### Smart devices
- Allow user interaction
- Smart devices perform fewer functions than a traditional client device
- ![](../assets/fb13b1a769a2146a3b1138b3c6a3bfeb.png)
### IoT, IIoT and ICS
- **Internet of Things (IOT)** networking of traditionally run non-computing physical objects and technologies in a consumer setting
	- Smart Fridge, thermostat,etc
- **Industrial internet of Things:** networking of traditionally non-computing physical objects and associated technologies like big data, artificial intelligence
- Industry-specific like utilities, food and oil refining
- **Supervisory control and data acquisition (SCADA):** ICS used to supervise machinery and industrial processes