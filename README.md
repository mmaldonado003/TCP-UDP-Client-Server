# TCP & UDP Client–Server File Transfer Project

**ALL FILES PERTAINING TO THE PROJECT CAN BE VIEWED ABOVE.**

---

## Objective

While understanding TCP and UDP conceptually is fundamental to networking, it is another challenge entirely to design, implement, and analyze these transport protocols firsthand.  
This project demonstrates both the reliable connection-oriented behavior of TCP and the connectionless, best-effort nature of UDP through practical experimentation.  
The goal was to build each protocol from scratch in Python, execute data transfers between remote Linux machines, and measure reliability, throughput, and data integrity across multiple test iterations then comparing results.

The idea for this project originated from my continued access to the University of Texas Computer Science account after graduation, which allowed me to remotely connect to UT CS lab machines and design, test, and complete this project.

---

## Setup

**Server:**  
Linux machine (**key**) acting as the central receiver for all data transmissions.

**Clients:**  
Three UT CS lab machines accessed remotely via SSH and VPN to send specific books to server:

- `agate` → *War and Peace*  
- `diamond` → *Pride and Prejudice*  
- `life` → *Robots of the World Arise!*

**Remote Environment:**

- Connected securely through Cisco VPN and VS Code’s Remote Explorer / Remote SSH extensions.  
- Allowed direct editing, execution, and monitoring of client and server code from an off-campus PC.

**Implementation Details:**

- Written entirely in Python, using the `socket` module.  
- Data sent in 2048-byte chunks.  
- Each client transmitted its book file to the server, which aggregated and logged results.  
- Both client-side and server-side logs were recorded for three full iterations of each protocol.

---

## File Organization

Each protocol and iteration were stored in clearly structured folders for traceability.

**Example:**

- `TCP_agate_War_iter1` — client-side log and data for *War and Peace* (Iteration 1)  
- `TCP_received_books_iter1` — aggregated data received on the server  
- `TCP_server_iter1_log` — detailed server-side connection and performance log  

Similarly:  
- `UDP_agate_War_iter1`, `UDP_received_books_iter1`, and `UDP_server_iter1_log` follow the same pattern for UDP testing.

---

## Process

1. **Server Setup:**  
   The server script was started on *key* to listen for incoming TCP or UDP connections.

2. **Client Execution:**  
   Each remote client was connected via SSH, transmitting its respective book file using the designated protocol.

3. **Data Transfer:**  
   Clients sent data in chunks, while the server recorded total bytes received, elapsed time, and throughput.

4. **Iteration:**  
   The process was repeated three times per protocol, producing consistent data for comparison.

---

## Results

### TCP Results

| Iteration | Total Bytes Server Received | Total Lines Server Received | Avg Throughput (KB/s) | % Data Loss |
|------------|-----------------------------|-----------------------------|------------------------|--------------|
| 1 | 4,189,952 | 81,847 | 73,380 | 0% |
| 2 | 4,189,952 | 81,847 | 78,539 | 0% |
| 3 | 4,189,952 | 81,847 | 76,736 | 0% |

**Reliable delivery:** No data loss across all iterations.  
*Note:* Total bytes of data server received directly coincides with total text lines server received from books, hence the values of both remain the same per iteration.

---

### UDP Results

| Iteration | Total Bytes Server Received | Total Lines Server Received | Avg Throughput (KB/s) | % Data Loss |
|------------|-----------------------------|-----------------------------|------------------------|--------------|
| 1 | 3,846,368 | 75,603 | 57.46 | 7.6% |
| 2 | 4,098,272 | 80,378 | 334.13 | 1.8% |
| 3 | 3,739,187 | 73,710 | 47.59 | 9.9% |

**Unreliable delivery:** Packet loss between 1.8%–9.9%, confirming UDP’s connectionless nature.  
*Note:* Total bytes of data server received directly coincides with total text lines server received from books, hence the percent of data lost is directly proportionate for both.

---

### Combined TCP vs UDP Comparison

| Protocol | Iteration | Total Bytes Server Received | Total Lines Server Received | Avg Throughput (KB/s) | % Data Loss |
|-----------|------------|-----------------------------|-----------------------------|------------------------|--------------|
| TCP | 1 | 4,189,952 | 81,847 | 73,380 | 0% |
| TCP | 2 | 4,189,952 | 81,847 | 78,539 | 0% |
| TCP | 3 | 4,189,952 | 81,847 | 76,736 | 0% |
| UDP | 1 | 3,846,368 | 75,603 | 57.46 | 7.6% |
| UDP | 2 | 4,098,272 | 80,378 | 334.13 | 1.8% |
| UDP | 3 | 3,739,187 | 73,710 | 47.59 | 9.9% |

---

## Analysis

### TCP Performance

- Achieved 0% data loss across all tests.  
- Consistent throughput and stable performance.  
- Validated the reliability mechanisms of TCP (ACKs, retransmission, congestion control).

### UDP Performance

- Demonstrated faster raw transfer rates in brief intervals, but overall lower integrity.  
- Significant data loss due to packet drops and unordered delivery, as expected for a connectionless protocol.  
- Multiple iteration variability provided tangible insight into real-world network unpredictability, even at a small scale.

### Observed Findings

These experiments reinforced theoretical knowledge of networking protocols through firsthand implementation, analysis, and comparison.

---

## Technical Skills Developed

- TCP and UDP socket programming in Python  
- Remote system administration using SSH and VS Code Remote Explorer  
- Secure VPN-based access to distributed systems  
- Data transmission logging, aggregation, and throughput analysis  
- Real-world validation of transport-layer reliability principles
