---
title: Chapter 4
---
## 4.1 Types of network addresses

### Types of network adresses
- **Physical address (media access control address- MAC)**: A unique 48-bit number burned into a network interface controller. A MAC address identifies a device or network
- **Logical address or Internet protocol address:** 32-bit or 128-bit number assigned to a network assigned to a network interface controller
- **Port or port number:** 16-bit unsigned number that uniquely identifies a network application or service on a host
### Port number
- Connections start and end with a port number
- Ex: webpages are associated with a different port than an email
- **Network protocol:** a set of rules specifying how data is formatted, processed, and transmitted between devices on a network (does not depend on OS,etc)

### Ports numbers
- **Well-known port** (privileged port or reserved port)
- **Registered port:** a port number between 1,024 and 49,151 that is registered with the internet assigned number authority (IANA for a specific use)
- **Ephemeral port (private port, higher number port, dynamic port)** is a port number between 49,152 and 65,535
- IP address has a TCP and UDP port

| Port number | Service                                              | Transport protocol |
| ----------- | ---------------------------------------------------- | ------------------ |
| 20, 21      | File Transfer Protocol (FTP)                         | TCP                |
| 23          | Telnet                                               | TCP                |
| 25          | SMTP                                                 | TCP                |
| 53          | DNS                                                  | UDP/TCP            |
| 67, 68      | DHCP                                                 | UDP                |
| 69          | TFTP                                                 | UDP                |
| 80          | HyperText Transfer Protocol (HTTP)                   | TCP                |
| 110         | POP3                                                 | TCP                |
| 123         | Network Time Protocol (NTP)                          | UDP                |
| 143         | IMAP                                                 | TCP                |
| 443         | HTTPS (Secure Socket Layer/Transport Layer Security) | TCP                |
| 445         | SMB                                                  | TCP                |
| 514         | Syslog                                               | UDP                |
| 993         | IMAPS                                                | TCP                |
| 995         | POP3 SSL                                             | TCP                |
| 1433        | SQL Server                                           | TCP                |
| 1521        | SQLNET                                               | TCP                |
| 2095        | Webmail                                              | TCP                |
| 3306        | MySQL                                                | TCP                |
| 3389        | RDP                                                  | TCP                |
| 5060, 5061  | SIP                                                  | UDP/TCP            |

## 4.2 MAC address

- **Media access control (MAC) address:** unique 48-bit identifier into a network interface controller
  - MAC address is burned into the the network interface controller by the manufacturer
  - **Organizationally unique identifier:** a 24-bit number uniquely identifying a particular piece of networking equipment from the manufacturer
  - **Device ID (vendor assigned identifier):** a 24-bit number concatenated to the OUI produce the full MAC address
    - Controlled by the manufacturer and can be compared to a serial number

- Typically represented as six groups of two-hexadecimal digits separated by hyphens or colons

### Mac address table

- Mostly used for forwarding data frames between devices on a local network
- **MAC address table:** maps each network devices MAC address to a switches physical port
- Static connection is manually entered in a MAC table
- Used by IEEE 802 network technologies

#### The Golden Rules of a Switch (AI)

1. **Flooding (Unknown Destination):** If a switch receives a frame and the destination MAC address is **not** in its MAC table, it doesn't know where to send it. To ensure it reaches the target, the switch "floods" (broadcasts) the frame out of **all active ports except the port it arrived on**.
2. **Forwarding (Known Destination):** If the destination MAC address **is** in the table, the switch sends the frame **only** out of the specific port listed.
3. **Learning:** A switch only adds a MAC address to its table by looking at the **source** MAC address of a frame it *receives*.

## 4.3 IPv4

### IPv4 address

- **IPv4 address** a unique 32-bit numeric address divided into four 8-bit octets
- **Loopback address (localhost):** an internal address that routes back to the local device
  - Adress is typically: `127.0.0.1`
- **Subnet mask:** a 32-bit number used to divide an IP address into a host portion and a network portion
  - Defines the range of host

### Classful addressing

- **Classful addressing:** an IPv4 addressing architecture that classifies IP addresses into five classes
  - **Class A address:** an IPv4 address class that uses the first 8 bits of a network and remaining bits for the host
  - **Class B address:** uses the first 16 bits for the network and remaining bits for the host
  - **Class C address:** uses the first 24 bits for the network and the remaining bits for the host
  - **Class D address:** an IPv4 address used for multicasting
  - **Class E address:** reserved for future use

### Public and Private IP addresses

- **Public IP address:** an IP address assigned to a host connected to the internet
- **Private IP address:** an IP address assigned to a host on a local network
- **RFC 1918 address:** an IP address assigned inside a private network

| Class   | Public IP ranges                                            |
| ------- | ----------------------------------------------------------- |
| Class A | 1.0.0.0 to 9.255.255.255 11.0.0.0 to 126.255.255.255        |
| Class B | 128.0.0.0 to 172.15.255.255 172.32.0.0 to 191.255.255.255   |
| Class C | 192.0.0.0 to 192.167.255.255 192.169.0.0 to 223.255.255.255 |

| Class   | Public IP ranges                                            |
| ------- | ----------------------------------------------------------- |
| Class A | 1.0.0.0 to 9.255.255.255 11.0.0.0 to 126.255.255.255        |
| Class B | 128.0.0.0 to 172.15.255.255 172.32.0.0 to 191.255.255.255   |
| Class C | 192.0.0.0 to 192.167.255.255 192.169.0.0 to 223.255.255.255 |

## 4.4 IPv6 format

- **Internet protocol version 6:** unique 128-bit number assigned to a network interface controller
- Has 2^128 and 2^32 addresses avaliable
- **Network component:** First 64 bits. Used for routing and consists of two parts
  - **Prefix length:** is the first 48 bits of the network component
  - **Subnet ID:** last 16 bits of the network component. A subnet ID describes the private topology
- **Node component:** IPv6 addresses last 64 bits. Node component is used to uniquely identify a device on a network

![img](https://zytools.zybooks.com/zyAuthor/NetworkPlus/10/IMAGES/c92ec9c6-3a1d-3dc2-63eb-a67e39a45baa)

**Rules:**

1. Leading zeros are removed within each hexadecimal group
2. Two or more hexadecimal groups containing all zeros are replaced with (occurs once per address)
3. Hexadecimal group containing all zeros is replaced with a single zero

### IPv6 supported address types

- **Unicast address:** a logical identifier representing a single network device. Unicast transmission sends IP packet data to a single destination
- **Multicast address:** a logical identifier representing a group of network devices. Sends IP packet data to a group of destinations simultaneously
- **Anycast address:** an address assigned to multiple network interfaces. Sends IP packet data to one network device in the group
  - Usually used by servers in a content delivery network
  - **Content delivery network or Content distribution network (CDN):** Geographically distributed group of servers
- **Broadcast address:** a single IPv4 address used to send data to all devices on a network



### IPv6 advantages and differences vs IPv4

- IPv4 addresses have specific public and private ranges of addresses 
- Public IPv6 address is accessible by outside network
- Private IPv6 is used in private local networks
- IPv6 allows aggregation of network prefixes into a single prefix and announces this one prefix to outside IPv6 net
- Can auto-configure when connected to other IPv6 devices

| Feature                   | IPv4 | IPv6                   |
| ------------------------- | ---- | ---------------------- |
| Subnet mask               | Yes  | No, uses prefix length |
| Uses classful addressing  | Yes  | No                     |
| Integrated IPSec          | No   | Yes                    |
| Contain IP-level checksum | Yes  | No                     |
