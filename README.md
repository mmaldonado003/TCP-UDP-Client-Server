# TCP & UDP Client–Server File Transfer Project

**ALL FILES PERTAINING TO THE PROJECT CAN BE VIEWED ABOVE.**

---

## Objective
This project implements and compares TCP and UDP client–server architectures to analyze data reliability, throughput, and integrity across distributed systems. By conducting real-world file transfers between remote Linux machines, the project demonstrates key differences between reliable (TCP) and connectionless (UDP) transport protocols, which are foundational knowledge for designing efficient enterprise information systems.

---

## Methodology
- Implemented using Python socket programming with `SOCK_STREAM` for TCP and `SOCK_DGRAM` for UDP  
- Data transmitted in 2048-byte chunks using identical test procedures for both protocols  
- Comprehensive logging captured:  
  - Client-side and server-side metrics per iteration  
  - Total bytes received, throughput (KB/s), and data loss percentage  
- Each protocol was tested three times under identical network conditions to ensure consistency and comparability
  
---
## Setup

**Server:**  
Linux machine (`key`) acting as the central receiver for all data transmissions.

**Clients:** Three UT CS lab machines accessed remotely via SSH and VPN to send specific books to the server:  

- `agate` → War and Peace (3,281 KB)  
- `diamond` → Pride and Prejudice (735 KB)  
- `life` → Robots of the World Arise! (57 KB)  

**Remote Environment:**  
- Connected securely through Cisco VPN and VS Code Remote Explorer / Remote SSH extensions.  
- Allowed direct editing, execution, and monitoring of client and server code from an off-campus PC.

---

## File Organization
Each protocol and iteration were stored in clearly structured folders for traceability.  

**Example:**  
- `TCP_agate_War_iter1` — client-side log and data for War and Peace (Iteration 1)  
- `TCP_received_books_iter1` — aggregated data received on the server  
- `TCP_server_iter1_log` — detailed server-side connection and performance log  

Similarly, `UDP_agate_War_iter1`, `UDP_received_books_iter1`, and `UDP_server_iter1_log` follow the same pattern for UDP testing.

---

## Process
- **Server Setup:** Started the server script on `key` to listen for incoming TCP or UDP connections.  
- **Client Execution:** Each remote client connected via SSH and transmitted its respective book file using the designated protocol.  
- **Data Transfer:** Clients sent data in chunks, while the server recorded total bytes received, elapsed time, and throughput.  
- **Iteration:** Repeated three times per protocol to produce consistent data for comparison.

---

## Results

### TCP Results

| Iteration | Total Bytes Server Received | Total Lines Server Received | Avg Throughput (KB/s) | % Data Loss |
|-----------|----------------------------|----------------------------|----------------------|------------|
| 1         | 4,189,952                  | 81,847                     | 73,380               | 0%         |
| 2         | 4,189,952                  | 81,847                     | 78,539               | 0%         |
| 3         | 4,189,952                  | 81,847                     | 76,736               | 0%         |

**Key Finding:** 100% reliability, consistent throughput (70–80 KB/s).

### UDP Results

| Iteration | Total Bytes Server Received | Total Lines Server Received | Avg Throughput (KB/s) | % Data Loss |
|-----------|----------------------------|----------------------------|----------------------|------------|
| 1         | 3,846,368                  | 75,603                     | 57.46                | 7.6%       |
| 2         | 4,098,272                  | 80,378                     | 334.13               | 1.8%       |
| 3         | 3,739,187                  | 73,710                     | 47.59                | 9.9%       |

**Key Finding:** Variable reliability (1.8–9.9% loss), unpredictable throughput (47–334 KB/s).  
**Note:** Iteration 2 showed a short-term throughput spike due to favorable network conditions, demonstrating UDP’s sensitivity to network congestion.

### Combined TCP vs UDP Comparison

| Protocol | Iteration | Total Bytes Server Received | Total Lines Server Received | Avg Throughput (KB/s) | % Data Loss |
|----------|-----------|----------------------------|----------------------------|----------------------|------------|
| TCP      | 1         | 4,189,952                  | 81,847                     | 73,380               | 0%         |
| TCP      | 2         | 4,189,952                  | 81,847                     | 78,539               | 0%         |
| TCP      | 3         | 4,189,952                  | 81,847                     | 76,736               | 0%         |
| UDP      | 1         | 3,846,368                  | 75,603                     | 57.46                | 7.6%       |
| UDP      | 2         | 4,098,272                  | 80,378                     | 334.13               | 1.8%       |
| UDP      | 3         | 3,739,187                  | 73,710                     | 47.59                | 9.9%       |

---

## Technical Analysis

### TCP Performance
- 0% data loss across all tests, validating TCP’s reliability mechanisms (ACKs, retransmissions, congestion control).  
- Throughput consistent at 70–80 KB/s, demonstrating stable performance.  
- Ideal for applications requiring complete data integrity.

### UDP Performance
- Higher burst throughput (up to 334 KB/s) but packet loss of 1.8–9.9%.  
- Missing or out-of-order chunks highlight tradeoff between speed and reliability.  
- Variation between iterations reflects network volatility.

### Combined Insight
- TCP provides stable, connection-oriented reliability with predictable performance.  
- UDP prioritizes speed over reliability, suitable for applications that can tolerate occasional data loss.  
- Protocol choice affects application performance, data accuracy, and user experience significantly.

---

## Business Recommendations

### Use TCP For Enterprise Workloads/Data
- File transfers and backups — zero data loss required  
- Database replication — data integrity critical  
- Financial transactions — full integrity REQUIRED
- Email and messaging systems — complete delivery expected  

**Advantages:**  
- Guaranteed delivery with 0% packet loss  
- Predictable throughput (70–80 KB/s) for capacity planning and SLA design  
- Built-in congestion control prevents network degradation

### Use UDP For Specific Low-Latency Applications
- Real-time streaming — video and VoIP where latency outweighs completeness  
- Online gaming — interactive systems tolerating occasional loss  
- DNS queries — lightweight, retryable network requests  
- Network monitoring — sampling-based data collection such as NetFlow

**Trade-offs:**  
- 1.8–9.9% data loss makes UDP unsuitable for critical workloads  
- Highly variable throughput (47–334 KB/s) depending on network conditions  
- Requires application-level reliability if completeness is needed

---

## Technical Skills Developed
- TCP & UDP socket programming in Python  
- Remote Linux system administration via SSH and VPN  
- Data logging, aggregation, and throughput analysis  
- Practical validation of transport-layer reliability principles

---

## Technical Details
Python 3.x | socket, threading, time | UT CS lab infrastructure | Cisco VPN + SSH access
