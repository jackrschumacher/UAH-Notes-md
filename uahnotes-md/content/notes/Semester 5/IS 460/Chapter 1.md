---
title: Chapter 1
---
## Chapter 1.1
- **Network:** Assortment of at least 2 connection points, nodes, capable of sharing resources through a link
- Topology is representation of the nodes in a network
	- Physical Topology - How network nodes are physically arranged
	- Logical Topology - How they are configured for communication
- A **single point of failure (SPOF)** is a critical business resource without redundancy and diversity.
- **Bandwidth** is the maximum amount of data a connection can transmit in a given amount of time.
- **Redundancy** is the duplication of a business resource to eliminate a SPOF.
### Topologies

#### Physical Topologies
- **Bus topology:** Physical network where nodes are connected to a single cable or bus
- **Ring topology:** Each node is connected to exactly 2 other nodes - forming a ring
- **Star topology:** Each node is connected to a central node, resembles a star or hub with spokes
- **Mesh topology:** A physical topology where each node is connected to every other node is a network
- **Hybrid topology:** A physical topology where at least 2 physical topologies are combined
#### Logical Topologies
- **Packet switched network:** network where the network parts, are configured to break down data into smaller packets
- **Control plane:** network plane that determines how a packet is transmitted
- **Data plane:** network plane that transmits a packet
- **Management plane:** the network plane that manages nodes

### Network mediums
- **Bounded media:** using cabling to transmit data through a narrow communication path
- **Unbounded media:** Network using wireless signal to transmit data through an open, or unbounded space

## Chapter 1.2
### Network models
- **Client:** Node that accesses a network resources from a server, but does not share network resources with other clients
- **Server:** a node that shares a network resource with a client
- **Peer:** a node capable of sharing and accessing a network resource with other peers
- 2 models
	- **peer-to-peer (p2p) model:** a network model consisting of peer nodes that share and access network resources from each other
	- **client-server model:** a network model consisting of at least one server that shares a network resource with at least one client
- Client-server networks are easier to scale than a P2P network
- P2P is easier to deploy because of self-managed node functions alone
#### Single location networks
- **Personal area network (PAN):** a small, single location network for a single user and the users personal networked devices
- **Local area network (LAN):** a small, single location network for multiple users and multiple networked devices
- **Wireless LAN (WLAN):** Devices communicating via unbounded media

#### Multilocation networks
- Single location can function alone or connect to another network
- **Metropolitan area network (MAN):** a large, multilocation network connecting at least two single locations networks for a city or muncipality
- **Campus area network (CAN):** a large, multilocation network connecting at least two single location networks for a school/corporate campus

#### Overlay networks
- Modern networks leverage at least one overlay network to improve network performance without an additional investment in network equipment
- **Overlay network:** a virtual abstraction layer built on top of an existing physical network infrastructure
- **Multiprotocol label switching (MPLS):** an overlay network technology that labels each data uses the label to find the quickest path to the data packets destination
- **Multipoint generic routing encapsulation (MGRE):** an overlay network technology that forms a point-to-multipoint tunnel to carry multiple protocols and traffic types over a single link
- **Software-defined network (SDN):** an overlay network technology that centralizes a single location networks management and control planes
- **Virtual extensible LAN (VXLAN):** An overlay network technology that extends the capabilities of locally-switched network over routed networks to improve network conditions among dedicated computing facilities 

### Chapter 1.3 Service providers

#### Service provider equipment
- **Service provider:** a vendor who provides telecommunications services
	- Must deploy the necessary equipment in a desired service area to attract potential customers
- **Service-related entry point:** where a service providers medium enters a customers premises
- **Demarcation point:** location where a service providers endpoint connects to a customers on-premise equipment
- **Smartjack:** a network interface device (NID) placed in a demarcation point to provide remote monitoring and other capabilities to a service provider 
- **Copper:** bounded media consisting of a copper core carrying electrical pulses
- **Fiber:** bounded media consisting of glass or plastic carrying light pulses

#### Service provider links
- **Digital subscriber line (DSL):** a telecommunications service delivering high-speed internet access using infrastructure
- **Cable:** telecommunications service delivering high-speed internet access using cable television infrastructure
- **Satellite:** a telecommunications service delivering high-speed internet access using LEO satellites and a dish (or phone) at the customers location
- **Leased line:** a telecommunications service delivering high-speed internet access using a customer-specific connection
- **Metro-optical:** a telecommunications service delivering high-speed internet access using fiber
- 