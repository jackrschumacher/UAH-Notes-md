---
title: Chapter 5
---
## 5.1 - Network Segmentation

### Segmentation
- **Segmentation:** process of dividing a single network into physical or logical network subset, known as a **subnetwork (subnet)**
- Used for performance improvement, access control, and stability
- **Physical segmentation:** segments a network with a networking device or hardware (ex: Deployment of multiple switched or a firewall)
- **Logical Segmentation:** segments a network with a configuration (Ex: Deploying multiple subnet masks)

### Physical segmentation

- Can be physically segmented intentionally or as a result of connecting networked devices to multiple network devices
- Connecting PCs to multiple different switches physically segments into multiple subnets until a crossover cable connects the switches together
- Physically segmenting network ensures that devices that should not communicate with each other can not communicate with each other unless connected physically
- Use cases:
  - Installation of more checkpoints for improved network monitoring
  - Improvement in performance lessening congestion on subnets
  - Implementation of hierarchical, segmented network to eliminate flaws of flat network
  - Reduction of attack surface as networks are separated physically
  - Accelerated of problem resolution by easily identifying problematic segments

### Logical segmentation

- Network can be logically segmented at layer 2 and layer 3 for same reasons a network is physically segmented
- Physical and logical segmentation are often used together to leverage benefits of segmentation type
- Ex: Physically segment network with firewall and logically segmenting network into multiple security zones through firewall configuration
- Usually segmented through VLANs
- **Virtual Area Network (VLAN):** logical segmentation configuration used to create at least logical network segment for performance improvement and resource control
  - Typically configured on a switch
  - Some VLAN elements are also configured on a router



## 5.2 - Binary Decimal Convers

### Binary number format

- Number expressed in base-2 numeral system
- **Bit (Binary Digit):** single digit binary number (Represented by a zero or one)
- Binary bit column will be labeled with a bit number and has associated decimal value
	- Bit number or bit column is interchangeable
	- Each binary bit column will be labeled with a bit number and has associated decimal value
	- Bit number or bit column are interchangeable
	- Bit column number of the rightmost bit in a binary number is bit 1
	- Bit number to the left is bit 2
	- Either 1 or 0 
	![](../assets/9b9f98b2ef9b0a6c769e981fca0d2326.png)
### Converting decimal to binary
- Transfer decimal number to decimal comparison number. Running counter used to subtract each binary digit until decimal comparison number is 0. Start with farthest left binary bit of binary number, loop
	- If decimal comparison number is 0, place a zero in the remaining bits of the 8-bit binary number
	- Binary bits decimal value than decimal comparison number, place a 0 in the binary bit column of the converting bit number
	- Binary bits decimal value is less than or equal to the decimal comparison number, place a 1 in the binary bit column of the converting binary number. Subtract decimals bit value from the decimal comparison number to obtain the difference. Difference is the new decimal comparison number
- Perform above steps for bits 7,6,5,4,3,2 and 1 until decimal comparison number is 0

## 5.3 - Network address

### Network address definition
- **Binary ANDing** the process of multiplying two binary numbers. ANDing the binary IPv4 address and binary subnet mask, an operation using the subnet mask and IPv4 address, produces a network address or network ID
	- Also identifies the networks host address range and the network segment
- **Network segment:** portion or segment of a network
- **Network address:** first address in the network segment and identifies the device network segment or subnetwork
- **Subnets (subnetworks or network segments):** logical, smaller partitions of a network

### Network and gateway address
- Devices that have a different network address, or are on different subnets, cannot exchange data directly
- Routers local IP address is the gateway IP address assigned to local devices on the subnet
- **Gateway IP address  (default gateway address):** local network devices address that transmits network packets to outside networks
- When devices sends and IP packet, device compares destination packets network address with the device's network address. If destination device's IP address is on the same network segment as sending device, packet is sent over local network. If destination devices IP address is on separate network segment, IP packet forwarded to sending devices gateway IP address

### Finding the network address
- ANDING an IP4 address and subnet mask produces the network address
- Special cases of ANDING
	- If any subnet masks octet is 11111111 or 255, corresponding IP address's octet is resulting address octet
	- If any subnet masks octet is 00000000 or decimal 0, resulting network address octet is 0

## 5.4 - Classless addresses

### Classless addresses
- **Classless addressing (classless inter-domain routing) (CIDR):** an addressing scheme using variable length subnet mask (VLSM)
- **Variable Length Subnet mask (VLSM):** a subnet design using multiple masks in the same network
- Classless addressing was to alleviate the IPv4 address shortage

| Characteristic       | Advantage                                                    |
| -------------------- | ------------------------------------------------------------ |
| Conserves IP address | Provided time for the transition to IPv6                     |
| Flexibility          | Allows administrators to create networks best suited to the business. The segments are based on powers of 2. |
| Speed                | Enables the creation of IP blocks tailored to the organization's size, helping to limit network traffic. |
| Security             | Allows network devices to be separated into different networks, adding an extra layer of security. |

### CIDR notation
- IP address is divided into two segments: network segment which identifies a whole network or subnet, and the host segment, which specifies the specific network IP address range
- Network segment is used for traffic routing between IP networks, and the host segment is used for traffic routing between IP networks, and the host segment is used for address allocation. CIDR notation is used to identify network and host segments
- CIDR notation: IP/ Bits allocated for network segment 

### CIDR function
- Alternative to classful addressing
- Allocated IP addresses more efficiently than classful addressing by allowing any number of contiguous bits in the IP address to identify a network ID. 
- CIDR notation works same for a VLSM as with a classful subnet mask
- Network bit number segment for a classful design is either 8,16 or 24 on the IP default address
- VLSM the number of bits allocated to subnet mask network ID is variable and obtained by counting number of bits allocated to network segment

| CIDR | Subnet mask     | Number host bits | Formula to calculate number of IP address | Total host IP addresses (subtract two for network and broadcast address) |
| ---- | --------------- | ---------------- | ----------------------------------------- | ------------------------------------------------------------ |
| /0   | 0.0.0.0         | 32               | = 4,294,967,296                           | 4,294,967,294                                                |
| /1   | 128.0.0.0       | 31               | = 2,147,483,648                           | 2,147,483,646                                                |
| /2   | 192.0.0.0       | 30               | = 1,073,741,824                           | 1,073,741,822                                                |
| /3   | 224.0.0.0       | 29               | = 536,870,912                             | 536,870,910                                                  |
| /4   | 240.0.0.0       | 28               | = 268,435,456                             | 268,435,454                                                  |
| /5   | 248.0.0.0       | 27               | = 134,217,728                             | 134,217,726                                                  |
| /6   | 252.0.0.0       | 26               | = 67,108,684                              | 67,108,862                                                   |
| /7   | 254.0.0.0       | 25               | = 33,554,432                              | 33,554,430                                                   |
| /8   | 255.0.0.0       | 24               | = 16,777,216                              | 16,777,214                                                   |
| /9   | 255.128.0.0     | 23               | = 8,388,608                               | 8,388,606                                                    |
| /10  | 255.192.0.0     | 22               | = 4,194,304                               | 4,194,302                                                    |
| /11  | 255.224.0.0     | 21               | = 2,097,152                               | 2,097,150                                                    |
| /12  | 255.240.0.0     | 20               | = 1,048,576                               | 1,048,574                                                    |
| /13  | 255.248.0.0     | 19               | = 524,288                                 | 524,286                                                      |
| /14  | 255.252.0.0     | 18               | = 262,144                                 | 262,142                                                      |
| /15  | 255.254.0.0     | 17               | = 131,072                                 | 131,070                                                      |
| /16  | 255.255.0.0     | 16               | = 65,536                                  | 65,534                                                       |
| /17  | 255.255.128.0   | 15               | = 32,768                                  | 32,766                                                       |
| /18  | 255.255.192.0   | 14               | = 16,384                                  | 16,382                                                       |
| /19  | 255.255.224.0   | 13               | = 8,192                                   | 8,190                                                        |
| /20  | 255.255.240.0   | 12               | = 4,096                                   | 4,094                                                        |
| /21  | 255.255.248.0   | 11               | = 2,048                                   | 2,046                                                        |
| /22  | 255.255.252.0   | 10               | = 1024                                    | 1022                                                         |
| /23  | 255.255.254.0   | 9                | = 512                                     | 510                                                          |
| /24  | 255.255.255.0   | 8                | = 256                                     | 254                                                          |
| /25  | 255.255.255.128 | 7                | = 128                                     | 126                                                          |
| /26  | 255.255.255.192 | 6                | = 64                                      | 62                                                           |
| /27  | 255.255.255.224 | 5                | = 32                                      | 30                                                           |
| /28  | 255.255.255.240 | 4                | = 16                                      | 14                                                           |
| /29  | 255.255.255.248 | 3                | = 8                                       | 6                                                            |
| /30  | 255.255.255.252 | 2                | = 4                                       | 2                                                            |
| /31  | 255.255.255.254 | 1                | = 2                                       | 2                                                            |
| /32  | 255.255.255.255 | 0                | = 1                                       | 1                                                            |
- 3 special CIDR blocks
  - /0 - allows access to any IP address between 0.0.0.0 and 255.255.255.255
  - /31 - networks with this subnet mask can assign two IP addresses as a point-to-point link
  - /32 - IP address is the only address on the network. All IP traffic is forwarded to the gateway

## 5.5 - Subnetting basics
### Segmentation - Subnetting
- **Subnetting:** the process of dividing into smaller networks (subnets), borrowing bits from the IP address host segment to the network segment
- Subnetting and CIDR refer tot he same concept and can be interchanged
- Subnetting is implemented at organizational level using private IP addresses, CIDR is implemented at the ISP level using IP addresses

| Calculation item                  | Formula                                                      |
| --------------------------------- | ------------------------------------------------------------ |
| Network ID                        | Perform AND function on the IP address and subnet mask       |
| Broadcast address                 | Add 2^number -1 to the network ID                            |
| Address range of subnet           | First address of range = network ID. Last address of range = broadcast address. |
| Usable IP address range of subnet | First address of range = next address in sequence after the network ID. Last address of range = the address in sequence before the broadcast address. |
### Network and broadcast address
- Network address/network ID is the first IP address in the host network segment address range
	- Identifies the host's network segment or subnet
- **Broadcast address:** the last IP address in the host network segment address range defined by the network or subset
	- Used by a network host to send data to every host on the network
### Subnetting
- Subnets are created by borrowing bits from the IP address host segment
- Number of borrowed bits is the smallest n such that 2^n is greater than the number of desired subnets

| Needed subnets | Borrowed host bits | Subnets created | Subnet usable hosts                 |
| -------------- | ------------------ | --------------- | ----------------------------------- |
| 2              | 1                  | = 2             | -2 remaining host bits = -2^7 = 126 |
| 3-4            | 2                  | = 4             | -2 remaining host bits = -2^6 = 62  |
| 5-8            | 3                  | = 8             | -2 remaining host bits = -2^5 = 30  |
| 9-16           | 4                  | = 16            | -2 remaining host bits = -2^4 = 14  |
| 17-32          | 5                  | = 32            | -2 remaining host bits = -2^3 = 6   |
| 33-64          | 6                  | = 64            | -2 remaining host bits = -2^2 = 2   |
| 65-128         | 7                  | = 128           | -2 remaining host bits = -2^1 = 0   |

### Calculating subnet ID and range

- Translate CIDR to a Decimal Mask
  - Translate your CIDR notation into dotted-decimal subnet mask
- Calculate the Block Size
  - Subtract value of octet from 256
- Find the Subnet ID
  - Look at the value of the octet in the IP address
  - Find the largest multiple of the block size less than or equal to the number
- Determine the broadcast address
  - Always exactly 1 number less than the start of the next subnet
- Define the useable IP Range
  - Useable addresses sit between the subnet and broadcast address

| Binary network ID (New subnet occurs when a borrowed bit changes to 1) | Network ID    | Broadcast address |
| ------------------------------------------------------------ | ------------- | ----------------- |
| 11000000.10100000.00000001.00000000                          | 192.168.1.0   | 192.168.1.31      |
| 11000000.10100000.00000001.00100000                          | 192.168.1.32  | 192.168.1.63      |
| 11000000.10100000.00000001.01000000                          | 192.168.1.64  | 192.168.1.95      |
| 11000000.10100000.00000001.01100000                          | 192.168.1.96  | 192.168.1.127     |
| 11000000.10100000.00000001.10000000                          | 192.168.1.128 | 192.168.1.159     |
| 11000000.10100000.00000001.10100000                          | 192.168.1.160 | 192.168.1.191     |
| 11000000.10100000.00000001.11000000                          | 192.168.1.192 | 192.168.1.223     |
| 11000000.10100000.00000001.11100000                          | 192.168.1.224 | 192.168.1.255     |