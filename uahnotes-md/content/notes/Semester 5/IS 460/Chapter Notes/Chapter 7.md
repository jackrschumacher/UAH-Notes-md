---
title: Chapter 7
---
## 7.1 - Network Transmission

### Broadcast, multicast, and unicast

- **Cast:** the transmission of packets across network media
  - **Unicast:** a cast to a single network device
  - **Multicast:** a cast to a group of network devices simultaneously
    - Sent to a subset of devices interested in receiving the information	
  - **Broadcast:** a cast to all devices on the network simultaneously



### Broadcast and collision domains 

- **Broadcast domain:** a logical network segment that includes all devices that receive broadcast traffic at layer 2. Switch ports are in the same broadcast domain, all router ports are in different broadcast domains
- **Collision domains:** where packet collisions occur in a network
  - **Collision:** layer 2 problem where at least two frame transmission collide and require retransmission
  - Each switch, bridge, router port is a separate collision domain 
  - Each hub port is in same collision domain

### MTU

- **Maximum transmission unit (MTU):** largest protocol data unit (PDU) frame size in a layer 3 transaction
  - Smaller MTU reduces network delay and a larger MTU reduces overhead
  - MTU specified in terms of bytes or octets and based on largest PDU layer can transmit
  - MTU for an ethernet frame is 1,500 bytes
- Data and physical layers usually add overhead to network layer data, MTU is maximum frame size of a medium minus amount of overhead
  - Ethernet maximum frame size is 1,518 with an MTU of 1,500 bytes and overhead of 18 bytes
- **Jumbo frame:** an Ethernet frame with a payload greater than standard MTU of 1,500 bytes
  - Jumbo frames, associated with OSI models data link layer is used on 1 Gbps local area of network
    - Maximum frame size 9,000 bytes

### CSMA

- **Carrier Sense Multiple Access (CSMA):** medium access control protocol designed to decrease a network collisions
  - High collision decreases network performance because of required retransmissions
  - Prioritizes decreasing collisions - eliminating collisions is not possible
  - If carrier is sensed, device will wait for transmission to finish before starting a new one
- CSMA types:
  - **Carrier sense multiple action/collision detection:** MAC sublayer protocol used to prevent collisions by sending a jam signal when collision detected
  - **Carrier sense multiple access/collision avoidance:** MAC sublayer protocol used to avoid collisions by using signals- request to send (RTS) and clear to send (CTS) before transmission

## 7.2 - Network Traffic

### Traffic Shaping

- **Traffic shaping (packet shaping):** a bandwidth management technique prioritizing the flow of network traffic. Traffic shaping prioritizing the flow of higher priority traffic over lower priority traffic
- 2 management techniques:
  - **Quality of Service (QoS):** prioritizes traffic of resource-intensive applications at L3
  - **Class of Service (CoS):** prioritizes traffic of resource- intensive applications at L2. Prioritizes traffic by group, allocating different levels of priority to different groups 
    - VoIP traffic is higher priority than HTTP

### VPN traffic modes: Split tunnel vs Full tunnel

- Ease of use makes VPNs more popular than other tunneling solutions
- Two tunneling modes:
  - **Full tunnel:** routes and encrypts network traffic through the VPN, regardless of where the VPN service is hosted. More recommended because all network traffic is encrypted
  - **Split tunnel:** routes and encrypts all non-internet network traffic over the VPN. Traffic doing to internet sites bypasses the VPN tunnel in split tunnel mode. Allows routing of some device or app traffic through a tunnel while still allowing local device access
    - Can protect confidential data without losing access to local network devices

### Network loop prevention

- **Network loop (L2 loop, bridge loop):** network topology in which more than one path exists between 2 network endpoints. Network loop occurs at L2 (data link)
  - Ex: network loop exists if more than one path exists between2 hosts on LAN
- Switch forwards broadcasts and multicasts to every switch ports, network loop causes a switch to repeatedly rebroadcast broadcast and multicast packets
- **Broadcast storm (network storm):** occurrence of a large number of broadcast and multicast packets on network within a short time. Degrades network performance by exhausting network bandwidth
- **Broadcast storm prevention (storm control):** prevents or reducing packet rebroadcasts on a LAN. 
  - Methods include removal of network loops by disabling ports and limiting rate of broadcast traffic
- **Bridge protocol data unit (BPDU):** packet exchanged between switches on LAN to direct networks loops. BPDU is used by the spanning tree protocol (STP) to construct a loop-free logical topology for a LAN. Should only be sent by switch. End devices connected to a switch port should be prevented from sending a BPDU packet
  - Attackers can use a switch port to inject malicious BPDU packet into LAN to modify network logical topology to manipulate L2 traffic. 
- **Bridge protocol data unit (BPDU):** is a control mechanism for preventing BPDU packet from entering the switch port. Protects L2 STP topology

### Spanning tree protocol

- Network topology often resembles a tree with a central node acting as a trunk. Other nodes connect to the trunk as branches and leaves
- **Spanning Tree protocol (STP):** is a network protocol for L2 devices uses to eliminate a loop 
  - Features:
    - Eliminates existing loops in network tree
    - Reconfigure network tree whenever a network change occurs
    - Increases a network tree's fault tolerance
- STP convergence time is relatively slow. 
- **Rapid spanning tree protocol (RSTP):** network loop eliminating network protocol with a fast convergence time than STP. Convergence time is less than 10 seconds
  - When switches in the initial state the port state is set to discarding, in convergence state is learning, if no loops are present - forwarding
- IEEE standardized and RSTP. RSTP is backward compatible with STP
  - IEEE 802.1D = STP and IEEE 802.1w

## 7.3 - Switch Features

### Switch port configurations

- Network switch is a smart device that functions as a multiport network bridge by receiving and forwarding data packets from the source of information to the destination device. Send data packets to designated destination ports using MAC addresses. 
  - 3 types of ports
    - Access port
    - Trunk port
    - Hybrid port
- Physical switch port can connect to various devices - device needs vary. Switch ports are individually configurable
  - Configurations
    - Speed
    - Duplex
    - Flow control
    - Port security
    - Port aggregation
    - Port mirroring

### Port mirroring

- **Port mirroring (Switched Port Analyzer/Roving Analysis Port-RAP):** network switched function used to send a copy of network packets transmitted over one switch port to other switch port for packet monitoring or analyzing. Can be used to mirror inbound or outbound network traffic or both
  - Implemented in LAN, WLANs, VLANs to identify, monitor, and troubleshoot network issues. 
  - Destination port is connected to monitoring or security application that analyzes or debugs data packets. Commonly used in network appliances that require monitoring of network traffic

### Port security

- **Port security:** secures a network by preventing unknown devices from forwarding packets. Security increased by limiting access to a switch port with a list of MAC addresses. Can be configured statically and dynamically. 
- Port security benefits:
  - Only packets that match the allowed port MAC address are allowed through. If it does not contain the MAC address, the packet is restricted or dropped
  - Limits number of MAC addresses for a given switch port
  - Secures network from unknown devices forwarding packets
  - Port security can be implemented on per-port basis

### Tagged and Untagged ports

- **Tagged port (trunk port):** a switch configured to carry traffic from multiple VLANs. Most common method for encapsulation for VLAN tagging is 802.1Q (Dot1q)- the tag is inserted into the ethernet frame - 4 bytes in size
- **Untagged port (access port):** switch port configured to carry traffic from single VLAN. Sends and receives traffic without without VLAN tagging
- **Native VLAN:** unused VLAN used to receive all untagged frames from untagged ports

## 7.4 - Switch configuration

### Switch configuration

- Switch configuration applied to an entire switch 
- Enables or disables a feature or service that a switch provides
- Common configurations:
  - Power over Ethernet (PoE)
  - Tagged ports
  - VLAN tunneling
  - Port duplex 
  - Port speed
  - Auto medium dependent interface (MDI) / medium dependent interface crossover (MDI-X) port feature
- **Power over Ethernet (PoE):** provides power and data to device using bounded media. Switch is either built to provide PoE or a separate module is installed to provide PoE. Device connected to PoE does not need traditional power providing cost savings
  - Ex: Wireless access points, stationary security cameras, VoIP phones
  - Can use a POE injector as well

### POE+

- **Power over Ethernet plus (PoE+):** series of PoE improvements that carry higher power amounts. Has a 30W maximum power output. PoE++ can power devices that require even more power
  - Ex: Wireless Access points, PTZ cameras, Video IP phones, Alarm systems

| IEEE standard                      | Maximum power rating | Device power available | Supported cable |
| ---------------------------------- | -------------------- | ---------------------- | --------------- |
| 802.3af Type 1 - PoE               | 15.4 W               | 12.95 W                | CAT3 and above  |
| 802.3at Type 2 - PoE+              | 30 W                 | 25.5 W                 | CAT5 and above  |
| 802.3bt Type 3 - 4PPoE/PoE++       | 60 W                 | 51 W                   | CAT5 and above  |
| 802.3bt Type 4 - 4PPoE/ PoE++/UPoE | 100 W                | 71 W                   | CAT5 and above  |

### LCAP

- **Link aggregation:** combines multiple network connections in parallel allowing increased throughput and link redundancy. Used mostly when connecting a switch to another switch, server, NAS or multi-port AP
- **Logical aggregation group (LAG):** single logical channel created when using link aggregation to combine physical connections
- **Link Aggregation Control Protocol (LACP):** specified by IEEE 802.3ad, provides standard negotiated method allowing switches to create and enable aggregated link
- Concepts:
  - **LACP system priorities:** determine the sequence in which 2 end devices select active interfaces to join a link aggregation group
  - **LACP interface priorities:** selects which Ethernet-trunk interfaces are active interfaces and assigns a priority number value
  - **LACP mode (M:N):** M is the number of active links, N is the number of back-up links- allows high reliability and load-balancing traffic

### VLAN tunneling

- **VLAN tunneling (802.1Q tunneling):** used by a service provider to segregate customer traffic through the addition of a second VLAN 802.1Q tag entry to a tagged frame
  - Tagged customer traffic is sent through a 802.1Q trunk port and enters service providers edge switch through a tunnel port
  - Each customer gets a separate VLAN tunnel ID to separate them from other customers. VLAN 802.1Q tag entry differentiates one customers traffic from another. Each customer configures a link on edge device back to the service provider.
    ![](../assets/d12a0a19c980ff9f505c26160c841e02.png)



## 7.5 - VLANs

### VLAN use case

- Can overcome limitations of physical network locations, provide access control, improve performance. 
- Can be used to segment organizations/users to improve security and performance
  - Can be used restrict employees resources based on job title, etc

### VLAN types

- Determines the intended use of a VLAN
- **VLAN database:** file a switch uses to store VLAN information
  - **Default VLAN:** preconfigured VLAN type for all switch ports, allow device to communicate with other connected devices
  - **Data VLAN:** defined VLAN type for carrying user-generated traffic (ex: email or web browsing)
  - **Voice VLAN:** defined VLAN tailored for voice traffic
  - **Management VLAN:** defined VLAN providing administrative access to a switch
  - **Native VLAN:** unused VLAN used to receive all untagged frames from untagged ports

### VLAN membership types

- Assigns membership type assigns a host to a logical network host
  - **Port-based VLAN (interface-based VLAN or static VLAN):** VLAN in which host connected to a specific switch port assigned to a specific VLAN. Port-based VLANs work at L1
  - **MAC-based VLAN:** a VLAN in which a hosts MAC address is used to assign host to VLAN. MAC based VLANs work at L2
  - **Protocol-based VLAN:** VLAN in which protocol types used to assign a host to VLAN Protocol based VLANs at L3

### VLAN connection types

- **VLAN-aware device:** device that understands VLAN membership
- **VLAN-unaware device:** a device that does not understand VLAN membership or format
- Three ways to connect a device to a VLAN:
  - **Trunk line** - all device connected to a trunk line must be VLAN-aware (thus the require VLAN )
  - **Access link** - access link connects a VLAN-unaware device to a VLAN-aware port
  - **Hybrid link**- hybrid link combines a trunk line and access link. A hybrid link connects both VLAN-aware and VLAN-unaware devices

## VLAN design and configuration

### VLAN deployment considerations

- Offers advantages of performance improvement, simplified implementation, access control. 
- Requires additional costs
- Enhances security but might introduce new threats
- VLAN specific threats:
  - **VLAN hopping:** a VLAN-specific attack where an attacker breaches a vulnerable VLAN and uses the breached VLAN to move or hop to other VLANs
  - **Switch Spoofing:** VLAN hopping variation where an attacker imitates (spoofs) a trunking switch - then can access multiple VLANs
  - **Double-tagging:** VLAN hopping variation where attacker bypasses VLAN-protecting mechanisms by tagging a frame with outer VLAN and inner, target VLAN

### VLAN security

- VLANs hinder unauthorized access and segmenting devices with sensitive data
- Provide protocol separation- limit traffic to the relevant VLAN
- Also extendable to wireless devices, ensuring consistency regardless of physical location

#### VLAN security best practices

| Best practice                                             | Justification                                                |
| --------------------------------------------------------- | ------------------------------------------------------------ |
| Assign one VLAN per access port                           | An access port should only carry traffic for a single VLAN   |
| Exclude all other VLANs from an access port               | Ensures a single VLAN uses an access port                    |
| Configure an access port as untagged                      | Mitigates double-tagging                                     |
| Exclude unwanted VLANs from a trunk port                  | Unwanted VLANs should not traverse a trunk port              |
| Configure a trunk port as tagged for all VLANs except one | Tagging ensures traffic reaches the correct VLANs - only the native VLAN receives untagged traffic |
| Configure a management VLAN                               | Segregates user traffic from administrative traffic          |
| Do not use VLAN 1                                         | VLAN 1 is a preconfigured VLAN an attacker can exploit       |
| Assign all ports to at least one VLAN                     | Unused ports can be exploited                                |
| Supplement VLAN routing with an access control list (ACL) | Provides an additional layer of packet filtering, limiting unwanted traffic |
| Assign the correct VLAN type to a port                    | Improves both performance and security                       |

### VLAN switch configurations

5 step configurations:

1. Enter configuration mode
2. Enter VLAN mode to create VLAN or range of VLANs
3. Exit VLAN mode
4. Confirm VLAN/VLAN range creation
5. Save the VLAN configuration to the VLAN database

- Creates one interface per VLAN
- **Switched virtual interface (SVI)/ VLAN interface:** a layer 3 interface created on a switch to provide communications between each configured VLAN
  - Act like default gateways for VLANs while also L2 and L3 protocols

### VLAN router configurations

- **inter-VLAN routing:** varies depends on the device and routing method used
  - Router with multiple physical ports can use one port per VLAN
  - **Subinterface:**  router can use a single physical port logically divided into multiple interfaces- each subinterface allows inter-VLAN routing. Router is configured with multiple sub-interfaces
  - L3 switch creates multiple SVIs with each SVI participating in inter-VLAN
- Each routing method used for inter-VLAN routing is somewhat comparable- selection depends on the network device needed 

### SVI

- SVI configurable on L2 and L3. SVIs configured on L2. SVI configured on L3 switches participate in inter-VLAN routing

## 7.7 - Security zones and IP support

### Demilitarized zones

- **Security zone:** a network segment containing network resources with the same trust level. L3 device used to establish security zones
  - 3 commonly deployed security zones:
    - **Trusted zone (private zone):** a security zone contains network resources that are only able to be accessed by an authorized user/system. Resources accessed from within the trusted zone automatically trust each other
    - **Untrusted zone (public zone):** security zone containing network resources between trusted and untrusted zones. Resources protects organizations trusted network resources from untrusted traffic
    - **Demilitarized zone (screened subnet):** security zone located between trusted zone and untrusted zone. Protects an organizations trusted resources from untrusted traffic. Commonly placed on public-facing assets

### NAT/PAT

- **Network address translation (NAT):** process of converting an inside IP address to a outside (public) address and allowing internet access to the network device
  - Operates at OSI L3, configured on a router or firewall device, allowing for additional network device security
  - Organizations that want multiple devices to employ a single IP address use NAT
  - Also used for IP address conservation
  - Routes multiple devices using one connection
- IPv6 NAT provides address translation between IPv4 and IPv6 addressed network devices
- **Teredo:** an IPv6 transition technology that provides tunneling when hosts are located behind IPv4 network address translators (NATs)
- **NAT64:** IPv6 mechanism for communication between IPv6 and IPv4 hosts. Translates between IPv4 and IPv6 protocols
- NAT types:
  - **Port address translation (PAT):** subnet of NAT, allows multiple private network devices to connect to the internet using the same IP address. Provides additional security by not exposing private IP
  - **Static NAT (one-to-one NAT):** provides one-to-one translation of inside local address to outside public address
  - **Dynamic NAT:** one-to-one IP address translation by mapping inside local address to an inside public address. Dynamic NAT translations show up in NAT table when router receives traffic that requires translation
  - **Source network address translation (SNAT):** technique that translates a source IP address normally a private IP address, to public IP address. SNAT is most common form of NAT used internal (private) host needs to map to external public host

### Dual Stack

- Until everyone switches to IPv6, devices need to provide IPv4/IPv6 support
- ISPs have all installed equipment installed with dual-stack technology
- **Dual-stack:** network device that can originate and understand IPv4 and IPv6 packets simultaneously
- **Dual-stack network:** is a network where all network devices can originate and understand IPv4 and IPv6 packets simultaneously 

## 7.8 - Routers

### Router basics

- Router is a device that connects 2 or more packet switched networks or subnetworks
  - Manages traffic between networks by forwarding packets toa  destination IP address
  - Router allows devices to use the same internet connection
  - Used to pass data between a LAN and a WAN
- Router uses a routing table to forward data. Default network destination address for the host systems default router is 0.0.0.0. Usually means that the network is locally connected on that interface
- **Time to live (TTL)/hop limit:** amount of time a packet is set to exist within a network before being discarded by a router
  - Enables the sender to receive information about a packet's route through the network and is useful in determining amount of time a packet has been in circulation
  - Each time the packet passes through a router or L3 device, TTL is reduced
  - If TTL reaches zero before the packet reaches the destination the packet is discarded

### Types of routers

- A wireless router uses an Ethernet cable to connect to a modem but does establish a LAN
- A WLAN (wireless local area network) connects multiple devices using wireless communication
- Wired router uses separate cables to connect one or more devices within the network, creates a LAN. 
- Allows devices in the network to access the environment

| Specialized router type | Characteristic                                               |
| ----------------------- | ------------------------------------------------------------ |
| Edge router             | Installed at the boundaries of a network. Distributes packets across multiple networks. |
| Core router             | Distributes packets within the same network rather than across multiple networks. |
| VPN router              | Is a normal router with VPN client software installed. Every VPN connected device is protected by the VPN. |

### Router mechanics

- Basic routing function is building a map of network using static or dynamic routing protocols
- Router that uses dynamic routing protocols notifies other network routers of topology of the network and network changes. Static routing does not adapt to network changes
- Static and dynamic routing protocol models build the map of the network - routing table
- **Router advertisement (RA):** local network transmission announcing routers IP address. Host uses RA to locate any local routers.
  - Any network device can broadcast an RA - Could be used to trick another computer into using it as a host
  - **Router Advertisement (RA) Guard:** a security feature used to block or reject rogue RA transmissions

### ACL security

- **Router access control list:** set of rules controlling which packets can pass through to the next hop or destination. Will inspect packet and based on rules will block or allow traffic flowing from the source to the destination.
- 2 ACL types:
  - **Standard ACL:** router ACL type controls traffic based on source IP address information
  - **Extended ACL:** router ACL type that controls traffic based on source IP address info, destination IP address info