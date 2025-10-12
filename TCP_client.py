"""
tcp_client.py
Maxmillion Maldonado
-------------
A simple TCP client that:
- Connects to a TCP server
- Sends file or stdin data in fixed-size chunks
- Prints debug info (bytes sent, throughput)

Usage:
python3 client-python.py [Server IP] [Server Port] < [filename]

To find server IP:
hostname -I
"""

import sys
import socket
import time

SEND_BUFFER_SIZE = 2048  # bytes per chunk


def client(server_ip, server_port):
    """
    Connect to the server and send data from stdin in chunks.
    Prints debug information for each chunk and total transfer stats.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server_ip, server_port))
            total_bytes = 0
            chunk_count = 0
            start_time = time.perf_counter()

            # Read stdin in chunks and send to server
            while True:
                data_chunk = sys.stdin.buffer.read(SEND_BUFFER_SIZE)
                if not data_chunk:
                    break
                client_socket.sendall(data_chunk)
                chunk_count += 1
                total_bytes += len(data_chunk)
                print(
                    f"[DEBUG] Sent chunk {chunk_count}, {len(data_chunk)} bytes",
                    file=sys.stderr
                )

            end_time = time.perf_counter()
            duration = end_time - start_time
            print(
                f"Sent {total_bytes} bytes in {duration:.2f} seconds "
                f"({total_bytes / duration / 1024:.2f} KB/s)",
                file=sys.stderr
            )
            print(
                "Client data sent. Check server for successful service.",
                file=sys.stderr
            )

    except socket.error as e:
        print(f"Socket error: {e}", file=sys.stderr)


def main():
    """Parse command-line arguments and run the client."""
    if len(sys.argv) != 3:
        sys.exit(
            "Executing Command: "
            "python3 client-python.py [Server IP] [Server Port] < [filename]"
        )

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)


if __name__ == "__main__":
    main()

