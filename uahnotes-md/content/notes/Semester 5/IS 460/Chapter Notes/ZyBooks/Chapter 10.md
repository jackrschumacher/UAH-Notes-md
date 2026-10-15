---
title: Chapter 10
weight: 10
---
## 10.1 - DNS

### Domain name system

- **Domain name:** unique name identifying an Internet resource. Consist of labels denoted by periods
- **Domain name system:** hierarchical, distributed naming system containing information for network resources
  - Translates domain names to IP addresses, allows users to connects to websites server resources
- **Domain namespace:** organized hierarchy of DNS administrative domains in the world
- **DNS zone:** segment of the domain hierarchy which is assigned to a legal entity
- Ways of securing DNS deployment
  - **DNS over TLS (DoT):** sends TLS protocol encrypted queries attached to the UDP protocol
  - **DNS over HTTPS (DoH):** sends encrypted queries/requests by HTTP or HTTP/2 protocols

### URL structure

- Defines a domain namespace, specifies top-level domains, second-level domains, lower-level domains (subdomains)
  - Each level can be a DNS zone
- Domain name levels/terms:
  - **Root domain:** highest internet hierarchical level.
    - Ex: Level above .com is displayed as a period
    - On individual/company sites- root domain refers to second-level domain with top-level domain
  - **Uniform resource locator (URL)/ web address:** specifies location of internets web reference.
    - Ex: jackrschumacher.com/about and jackrschumacher.com have the same server IP address, but different directory locations
  - **Hostname:** domain name with at least 1 associated IP address (Ex: www.jackrschumacher.com or [jackrschumacher.com](https://jackrschumacher.com)) 
  - **Fully qualified domain name (FQDN):** domain name specifying the exact location in DNS tree hierarchy 
    - Ex: www.jackrschumacher.com
  - **Top-level domain (TLD):** domain name's right-most label. 
    - Ex: the TLD of www.jackrschumacher.com is .com
  - **Second-level domain (SLD):** subdomain TLD left label. In a top-down structure, SLD is below the TLD
    - Ex: the SLD of www.jackrschumacher.com is jackrschumacher
  - **Subdomain:** an additional domains hostname. In a top-down structure is below the SLD
    - Ex: links is the subdomain of [links.jackrschumacher.com](links.jackrschumacher.com)

### Namespace database and RR

- DNS system organizes information in distributed database format for reliability and efficiency.
- **Namespace databases:** Information in a distributed database about DNS, stored in text files called DNS zone files
- **DNS resource record (RR):** unit of information in DNS zone files. RR contains specific information of zone. 
- Fields associated with DNS records:
  - Name: Specifies DNS name, also known as owner name
  - Time to Live (TTL): Time for any changes in DNS records to go into effect. 
    - Ex: TTL of 60 means that record is refreshed every minute
  - Address class: Defines RR protocol family
    - Ex: IN for internet addresses
  - Type: Defines type of resource record
    - Ex: A, NS, CNAME
  - Data length: Data field in octets
  - Data: Information in field dependent on record type

## 10.2 - DNS process

### DNS server types

- **DNS recursor:** receives queries from a client and starts the process to resolve domain name to an IP address. Device that responds to recursive request from a client, and returns a DNS record to the client through a series of requests
- **Root name server:** DNS nameserver that operates in a root zone, answers queries for records stored or cached within the root zone and referring to other request to the appropriate Top Level Domain server
- **Top-level domain (TLD) name server:** responsible for maintaining information about domain names sharing a common extension. Points query to authoritative DNS name server associated with query's domain
  - Ex: .com, .gov, .net
- **Authoritative name server:** answers DNS questions about names in a DNS zone 
  - Authoritative-only name server stores information about domain names specifically configured by the administrator
  - Can be configured to give authoritative answers to queries in some zones and act as a cache server in other zones
  - Can be a primary or secondary server
    - Primary server contains definitive versions of all records that zone that can be identified in the Start of Authority (SOA) record
    - Secondary server uses automatic updating mechanisms to maintain identical copies of primary servers database for a zone
    - Every domain name appears in zone serviced by one or more authoritative name servers
- **DNS caching:** DNS local temporary database containing lookup information for recently visited sites

### DNS records types

DNS records provide information about a domain

Common DNS resource records (RR) types:

| Record type | Definition                                                   | Example                                                      |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| A           | A **DNS A address** record maps a domain to an IPv4 address. | wiley.com maps to 192.168.10.254                             |
| AAAA        | A **DNS AAAA** (pronounced "quad-A") maps a domain name to an IPv6 address, functioning as the IPv6 equivalent of an A record. An IPv6 address is 128 bits — exactly four times the size of an IPv4 address. The four A's reflect that size relationship. | wiley.com maps to 4002:2460:2460:3333::1                     |
| CNAME       | A **DNS CNAME (canonical name)** maps an alias domain to a canonical name. | www.mycompany.com cname mycompany.com                        |
| MX          | A **DNS MX (MAIL EXCHANGE)** record directs email to a mail server. | mail.facebook.com                                            |
| PTR         | A **DNS PTR (pointer record)** maps an IP address to a domain name for reverse DNS lookup. | 65.65.85.120.in-addr.arpa maps to mail.mycompany.com         |
| ANAME       | An **ANAME** record points the root of a domain to an FQDN.  | www.mycompany.com zone record contains: @ (denotes root domain), Type: A, Address value: 65.65.85.12, and TTL: 7200. |
| SOA         | A **DNS SOA (start of authority)** record stores domain information. | Zone administrator's email.                                  |
| NS          | A **DNS NS (name server)** record contains the authoritative name server's name within a domain or DNS zone. | ns1.mycompany.com                                            |
| TXT         | A **DNS TXT** allows text to be entered that is associated with the domain. | Can be used to stop email spam by listing all the servers that are authorized to send email messages from the domain. |
| SRV         | A **DNS SRV (service)** specifies a host and port for specific services. Ex: VoIP. | _xmpp._tcp.mycompany.com. 43200 IN SRV 20 10 5223 server.wiley.com |

### DNS queries

- **DNS query:** request of DNS information from DNS client to a DNS server
- Three types of DNS queries
  - **Recursive DNS query:** when one DNS server communicates with several other DNS servers to resolve domain name to IP address
  - **Iterative DNS query:** a client client communicates directly with each DNS server involved in the lookup
  - **Non-recursive DNS query:** a query which DNS Resolver already knows DNS information from a cache or DNS Name Server query - authoritative server for the domain
- DNSSEC - set of extensions to DNS that provide a DNS that provide DNS resolver cryptographic extensions. Assigns every DNS zone a public-private key pair. Zone owner uses the zones private key to digitally sign DNS data in the zone. 

### DNS reverse lookup

- **Reverse DNS:** querying technique connecting the domain name with an IP address
  - Ex: An email server uses reverse DNS to validate authenticity of an email. Many servers reject messages not supported by reverse lookups
  - Use the special domain `in-addr.arpa`. In this, IPv4 address is obtained by reversing original 32-bit IPv4 address octet order. (Ex: 23.221.222.250 turns into 250.222.221.23) - points to the source IP and the destination IP

## 10.3 - DHCP

### DHCP basics

- Network device requires IP address and network configuration parameters
- Devices IP address and network connection parameters are set manually or automatically
- **Dynamic host configuration protocols:** a network management protocol used for automating the assignment of IP address and network configuration parameters 
- DHCP components:
  - **DHCP scope:** IP address and network configuration parameters a DHCP server makes available to a client
  - **DHCP server:** server configured to distribute DHCP scope to DHCP client
  - **DHCP client:** device configured to receive a DHCP scope from a DHCP server
- Common scope requirements:
  - IP address
  - Subnet mask
  - Default gateway
  - DNS server address
- UDP port 67 receives a DHCP clients request

### DHCP scope

- DHCP scope includes IP address from IP address range, or IP address pool.

- DHCP configuration parameters:

  - IP address of 192.168.100.10 from IP address pool of 192.168.100.0 to 192.168.100.200

  - Subnet mask of 255.255.255.0

  - **DHCP lease:** temporary assignment of a DHCP lease

  - DHCP server IP address of 192.168.100.2

  - Default gateway IP address of 192.168.100.1

  - DNS server IP address of 8.8.8.8

- **DHCP exclusion range:** IP address range a DHCP server cannot use for DHCP client requests
  - Ex: DHCP scopes IP address pool is 172.16.10.1-172.16.10.100 with DHCP exclusion range is 172.16.10.50-172.16.10.55. Addresses in the exclusion range are not offered to client devices

### DHCP allocation

- DHCP allocates IP addresses and network configuration parameters using 2 methods:
  - **Dynamic allocation:** DHCP method used to automatically assign DHCP scope to DHCP client
  - **DHCP lease reservation:** DHCP method used to assign a DHCP scope to DHCP client based on DHCP client MAC address
- Allocates a DHCP scope to DHCP client for time specified in DHCP lease. Default DHCP lease time is 24 hours. DHCP client can renew a DHCP lease before DHCP scope is returned for future use. DHCP lease information is stored in DHCP table. 
- **Automatic Private IP addressing (APIPA):** Windows feature providing DHCP autoconfiguration addressing when DHCP server is unavaliable. Pool is 169.254.0.0 to 169.254.255.255

DHCP lease time reccomendations:

| Device/location  | Recommended lease time | Reasoning                                                    |
| ---------------- | ---------------------- | ------------------------------------------------------------ |
| Wired devices    | 8 days                 | Stays on network longer - longer lease time reduces DHCP related traffic |
| Wireless devices | 1 Day / 24 hours       | Leaves network often for days. Regular devices will keep the same IP if connected daily |

 ### DHCP table and static IP assignments

- Static address might be beneficial for network addresses (Ex: routers, network printers, print servers, servers,etc.)
- Static default gateway address is usually assigned to provide the DHCP server to hand out the default gateway
- Static IP-address can be hard-coded in network device or DHCP reservation lease can be used
- Table is used when determining dynamic or static IP addresses. Contains information on client name, interface, IP information, connection status
- **IP Address management (IPAM):** administration tool used to manage DNS and DHCP changes. Plans, tracks and manages network IP address space

DHCP table format:

| Name    | Interface | IP address   | MAC address       | State        | Expire time |
| ------- | --------- | ------------ | ----------------- | ------------ | ----------- |
| PC      | LAN       | 10.10.10.150 | 1C:34:89:3F:06:B4 | Active       | 12:15:14    |
| AP      | LAN       | 10.10.10.151 | 1B:5D:75:76:4F:B6 | Active       | 09:15:44    |
| Laptop  | Wireless  | 10.10.10.152 | 38:34:76:4E:01:A7 | Disconnected | 19:20:22    |
| Printer | LAN       | 10.10.10.153 | 37:5A:78:38:18:B8 | Active       | 15:20:45    |

## 10.4- DHCP server and queries

### DHCP messages

DHCP server and DHCP client communicate using these messages:

- **DHCP discovery:** DHCP message broadcasted by DHCP client to discover DHCP servers on a network
- **DHCP offer:** DHCP message sent by DHCP server to offer DHCP client a DHCP scope
- **DHCP request:** DHCP message sent by DHCP client to accept DHCP offer
- **DHCP ack:** DHCP sent by DHCP server to acknowledge a DHCP request

### DHCP relay

- DHCP server may be located on different subnet than DHCP client. Router will not forward DHCP messages by default. 
- Two configurations allow DHCP messages to traverse different subnets:
  - **UDP helper address:** router configuration used to forward specified network traffic from one subnet to another subnet
  - **DHCP relay agent:** any node configured DHCP messages between different subnets

### SLAAC

- Automatically assigning IPv6 can be accomplished using DHCP or SLAAC

- **Stateless address autoconfiguration (SLAAC):** process allowing each network device to autoconfigure a unique IP address without a centralized device maintaining IPv6 configurations
- Creates a devices link-local address using EUI-64 method (extended unique identifier 64). IPv6 configuration method that creates link-local address using modified version of devices MAC address
- SLAAC with EUI-64 process
  1. Determine the device's 48-bit MAC address
  2. Insert FFEE in the MAC address to increase the bit size from 48 bits to 64 bits
  3. Invert the seventh bit, known as universal/local (U/L) bit
  4. Produce a link-local address

## 10.5- NTP

### Network time protocol

- **Timestamp:** used to identify the date and time of an event recorded on a computer/device
- NTP allows a computer to maintain accurate time calibrated to fractions of a second
- **Network time protocol (NTP):** a network protocol used to synchronize a devices system clock. Uses UDP port 123 and NTP clients use UDP port 1023
- **NTP timestamp:** is a 64-bit binary fixed-point NTP number using 32-bit part for seconds and 32-bit part for fractional seconds. 
- Essential to ensure aging for document retention
- **Precision Time Protocol (PTP):** network protocol used to synchronize time at nanosecond/picosecond level
- **Network time security (NTS):** standard used to secure NTP using TLS

### NTP time sources

- **Time server:** a device connected to a network that contains trusted time and provides accurate time to time and provides accurate time to clients using the UDP protocol. 
  - Available across the internet
- **Stratum:** a level of NTP hierarchical and represents distance to reference clock. Stratum levels 0-2 are used for NTP time synchronization
- **Stratum 0:** reference clock receiving time from an atomic clock or global positioning system (GPS) satellite. Generates an accurate pulse per second, triggers a timestamp
- **Stratum 1:** also known as a primary time server, a server whose system time, is synchronized to a stratum 0 device. May synchronize with other Stratum 1 time servers

### NTP client 

- Based on principle of synchronizing device to UTC. 
- Clients execute a program that queries a time server for a precise UTC time reference
- Queries performed at designated time interval to maintain sync accuracy
- NTP timestamps transfer 64-bit data packets between client and server
- Client uses NTP timestamps to determine difference between internal time and UTC time reference and adjusts local time to reference time. 
- Client can also determine network latency and apply correction factor when internal time is adjusted



## 10.6 - Amazon.com and DNS 

### Business challenges

| Challenge                    | Explanation                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| Normal high traffic volume   | Significant and often sudden surge in the number of normal DNS queries and responses processed by DNS servers |
| Global reach                 | Ability of a DNS service to provide fast and reliable domain name resolution to users across the world |
| Availability and reliability | Consistency and dependability of DNS services                |
| DDoS attacks                 | Malicious attempts to disrupt the normal functioning of a targeted server, service, or network by overwhelming with a flood of traffic |
